import json

import requests

from arch.common.base_utils import current_timestamp
from entity.item import FateVersionItem
from fate_manager.service import k8s_service
from fate_manager.service.k8s_service import get_node_ip
from fate_manager.utils.conf_utils import check_config
from fate_manager.operation.db_operator import DBOperator
from fate_manager.entity.types import (ProductType, IsValid, DeployType, PackageStatus, DeployStatus, ClickType,
                                       TestStatus, TestItem, ToyTestOnlyTypeRead, SiteRunStatus, ToyTestOnly,
                                       ToyTestOnlyRead, SiteStatus, RoleType, JobType, JobStatus, ServiceStatus)
from fate_manager.db.db_models import (DeploySite, ComponentVersion, FateVersion, KubenetesConf, DeployComponent,
                                       AutoTest, FateSiteInfo, DeployJob)
from arch.common.conf_utils import get_base_config
from fate_manager.settings import HYPERION_SETTINGS, TEST_PARTY_ID, WORK_MODE, DEPLOY_SETTINGS
from service import job_service


def get_component_list(request_data):
    deploy_site_objs = DBOperator.query_entity(DeploySite, party_id=request_data.get('partyId'),
                                        product_type=ProductType.FATE, is_valid=IsValid.YES,
                                        deploy_type=DeployType.HYPERION)
    if deploy_site_objs:
        version = deploy_site_objs[0].to_json().get('fate_version')
        components = DBOperator.query_entity(ComponentVersion, fate_version=version)
        res_list = []
        for component in components:
            component_info = component.to_json()
            res_list.append({
                'module': component_info.get('component_name'),
                'description': component_info.get('image_description'),
                'version': component_info.get('component_version'),
                'size': component_info.get('image_size'),
                'time': component_info.get('image_create_time'),
                'status': {
                    'code': component_info.get('package_status'),
                    'desc': PackageStatus.to_str(component_info.get('package_status'))
                }
            })
        result = {
            'list': res_list,
            'fateVersion': version
        }

        deploy_site = {
            'party_id': request_data.get('partyId'),
            'product_type': ProductType.FATE,
            'is_valid': IsValid.YES,
            'deploy_type': DeployType.HYPERION
        }
        DBOperator.update(DeploySite, {'fate_version': version}, deploy_site)
        return 0, 'success', result
    return 100, 'no data found', {'list': [], 'fateVersion': 0}


def get_auto_test(data):
    return DBOperator.query_entity(AutoTest, **data)


def get_deploy_component(data: dict):
    return DBOperator.query_entity(DeployComponent, **data)


def get_kubenete_url(deploy_type):
    sql = 'SELECT t1.id, t1.kubenetes_url, t1.node_list FROM t_fate_kubenetes_conf t1' \
          f'JOIN t_fate_deploy_site t2 on t1.id = t2.kubenetes_id and t2.is_valid = 1 and t1.deploy_type= {deploy_type}'
    query_res = DBOperator.query_with_raw_sql(sql)
    if query_res:
        return query_res[0]
    return None


def get_kubenetes_conf(deploy_type):
    instances = DBOperator.query_entity(KubenetesConf, deploy_type=deploy_type)
    if instances:
        return instances[0].to_json()
    return {}


def add_kubenetes_conf(kubenete_conf):
    DBOperator.create_entity(KubenetesConf, kubenete_conf)


def get_fate_version_list(fate_version):
    sql = 'SELECT fate_version FROM t_fate_version ' \
          f'WHERE fate_version = {fate_version} ' \
          'GROUP BY fate_version'
    query_res = DBOperator.query_with_raw_sql(sql)
    data = []
    if query_res:
        for item in query_res:
            data.append(FateVersionItem(id=item.id, fate_version=item.fate_version, chart_version=item.chart_version,
                                        pull_status=item.pull_status, version_index=item.version_index,
                                        package_status=item.package_status).to_dict())
    return data


def connect_hyperion(request_data):
    resp = requests.post(url=request_data.get('ansbileUrl')+HYPERION_SETTINGS.get('ConnectUri'))
    if resp.status_code == 200:
        conn_resp = resp.json()
        if conn_resp.get('retcode') == 0:
            kubenetes_conf = {
                'kubenetes_url': request_data.get('ansbileUrl'),
                'deploy_type': DeployType.HYPERION,
                'click_type': ClickType.CONNECT,
                'node_list': DEPLOY_SETTINGS.get('HYPERION_NODE'),
                'create_time': current_timestamp(),
                'update_time': current_timestamp()
            }
            conf = get_kubenetes_conf(DeployType.HYPERION)
            if not conf:
                return 100, 'no kubenete conf found'
            if conf.get('id') == 0:
                add_kubenetes_conf(kubenetes_conf)

            deploy_site = {
                "party_id": request_data.get('partyId'),
                "product_type": ProductType.FATE,
                "status": SiteRunStatus.UNKNOWN,
                "click_type": DeployStatus.LOADED,
                "kubenetes_id": conf.get('id'),
                "fate_version": conn_resp.get('fate_version'),
                "deploy_status": DeployStatus.UNKNOWN,
                "single_test": TestStatus.WAITING,
                "minimize_normal_test": TestStatus.WAITING,
                "minimize_fast_test": TestStatus.WAITING,
                "toy_test_only": ToyTestOnly.NO_TEST,
                "toy_test_only_read": ToyTestOnlyRead.YES,
                "deploy_type": DeployType.HYPERION,
                "is_valid": IsValid.YES,
                "create_time": current_timestamp(),
                "update_time": current_timestamp()
            }

            fate_version = conn_resp.get('fate_version')
            fate_version_list = get_fate_version_list(fate_version)
            if len(fate_version_list) > 0:
                deploy_site['version_index'] = fate_version_list[0].get('version_index')

            if conf.get('id') > 0:
                deploy_site['kubenetes_id'] = conf.get('id')

            if kubenetes_conf.get('click_type') > 0:
                deploy_site['click_type'] = conf.get('click_type')

            click_tag = False

            config = {
                'party_id': request_data.get('partyId'),
                'fate_version': conn_resp.get('fate_version'),
                'role': conn_resp.get('role'),
                'modules': {}
            }

            modules = []
            for offset, conn_item in enumerate(conf.get('data', [])):
                if conn_item.get('module') in ['clustermanager', 'mysql', 'nodemanager', 'fateflow', 'rollsite', 'fateboard']:
                    modules.append(conn_item.get('module'))
                    address = ''
                    address_list = []
                    click_tag = True
                    port = conn_item.get('port')
                    for ip in conn_item.get('ips'):
                        address_list.append(ip)
                        if conn_item.get('module') == 'fateflow':
                            address = f"{ip}:{conn_item.get('http_port')}"
                        else:
                            address = f"{ip}:{port}"

                    ip_node = {
                        'ip': address_list,
                        'port': port
                    }

                    if conn_item.get('module') == 'mysql':
                        config['modules']['mysql'] = {
                            'ip_node': ip_node,
                            'password': 'fate_pass',
                            'user': 'fate_user'
                        }
                    elif conn_item.get('module') == 'clustermanager':
                        config['modules']['clustermanager'] = ip_node
                    elif conn_item.get('module') == 'nodemanager':
                        config['modules']['nodemanager'] = ip_node
                    elif conn_item.get('module') == 'fateflow':
                        config['modules']['flow'] = {}
                        config['modules']['python'] = {
                            'ip': address_list
                        }
                        config['modules']['flow'] = {
                            'ip': address_list,
                            'dbname': 'fate_flow',
                            'grpc_port': 9360,
                            'http_port': port
                        }
                    elif conn_item.get('module') == 'fateboard':
                        config['modules']['fateboard'] = {
                            'dbname': 'fate_flow',
                            'ip_node': ip_node
                        }
                        config['modules']['java'] = {
                            'ip': ip_node['ip'],
                            'java': {
                                'ip': address_list
                            }
                        }
                        config['modules']['supervisor'] = {
                            'ip': address_list
                        }
                    elif conn_item.get('rollsite') == 'rollsite':
                        config['modules']['rollsite'] = {
                            'ip_node': ip_node,
                            'port': port,
                            'default_rules': [{
                                'name': 'default',
                                'ip': DEPLOY_SETTINGS.get('EXCHANGE_IP', ""),
                                "port": DEPLOY_SETTINGS.get('EXCHANGE_PORT', 0),
                            }],
                            'rules': [{
                                'name': 'default',
                                'ip': address_list[0],
                                "port": port,
                                },
                                {
                                    'name': 'fateflow',
                                    'ip': address_list[0],
                                    "port": 9360,
                            }],
                        }
                        config['modules']['eggroll'] = {
                            'ip': address_list,
                            'dbname': 'eggroll_meta',
                            'egg': DEPLOY_SETTINGS.get('SESSION_PROCESSOR_PER_NODE', 0)
                        }

                    deploy_component = {
                        'job_id': f"{request_data.get('partyId')}_connect",
                        'party_id': request_data.get('partyId'),
                        'product_type': ProductType.FATE,
                        'component_name': conn_item.get('module'),
                        'component_version': conn_resp.get('data', {}).get('fate_version'),
                        'address': address,
                        'deploy_status': DeployStatus.INSTALLED,
                        'is_valid': IsValid.YES,
                        'end_time': current_timestamp(),
                        'create_time': current_timestamp(),
                        'update_time': current_timestamp()
                    }

                    component_version_list = DBOperator.query_entity(ComponentVersion,
                                                                     fate_version=deploy_component.get('fate_version'),
                                                                     component_name=conn_item.get('module'))
                    if component_version_list:
                        deploy_component['version_index'] = component_version_list[0].get('version_index')
                        deploy_component['component_version'] = component_version_list[0].get('component_version')

                    if conn_item.get('status') == 'running':
                        deploy_component['status'] = SiteRunStatus.RUNNING
                    elif conn_item.get('status') == 'stopped':
                        deploy_component['status'] = SiteRunStatus.STOPPED
                    else:
                        deploy_component['deploy_status'] = DeployStatus.INSTALLED_FAILED
                        deploy_component['status'] = SiteRunStatus.UNKNOWN

                    deploy_component_list = get_deploy_component(deploy_component)
                    if not deploy_component_list:
                        DBOperator.create_entity(DeployComponent, deploy_component)

                    auto_test = {
                        'party_id': request_data.get('partyId'),
                        'product_type': ProductType.FATE,
                        'fate_version': conn_resp.get('data', {}).get('fate_version'),
                        'test_item': conn_item.get('module'),
                    }

                    auto_test_list = get_auto_test(auto_test)
                    if not auto_test_list:
                        auto_test['status'] = TestStatus.WAITING
                        DBOperator.create_entity(AutoTest, auto_test)
                    else:
                        data = {
                            'status': TestStatus.WAITING
                        }
                        DBOperator.update(AutoTest, data, auto_test)

                    if offset == len(conn_resp.get('data', [])):
                        auto_test['test_item'] = ''
                        job_service.insert_test_item(auto_test, auto_test_list, TestItem.TOY)
                        job_service.insert_test_item(auto_test, auto_test_list, TestItem.FAST)
                        job_service.insert_test_item(auto_test, auto_test_list, TestItem.NORMAL)
                        job_service.insert_test_item(auto_test, auto_test_list, TestItem.SINGLE)

            deploy_site_list = DBOperator.query_entity(DeploySite, **deploy_site)
            if not deploy_site_list:
                if click_tag:
                    deploy_site['click_type'] = ClickType.INSTALL,
                    deploy_site['deploy_status'] = DeployStatus.INSTALLED

                    if len(config.get('role')) == 0:
                        site_info = {
                            'party_id': deploy_site.get('party_id'),
                            'status': SiteStatus.JOINED
                        }
                        site_info_list = DBOperator.query_entity(FateSiteInfo, **site_info)
                        if len(site_info_list):
                            config['role'] = RoleType.to_str(site_info_list[0].get('role'))

                    deploy_site['config'] = json.dumps(config)

                    deploy_job = {
                        'job_id': f"{request_data.get('partyId')}_connect",
                        'job_type': JobType.INSTALL,
                        'creator': 'admin',
                        'status': JobStatus.SUCCESS,
                        'start_time': current_timestamp(),
                        'end_time': current_timestamp(),
                        'party_id': request_data.get('partyId'),
                        'deploy_type': DeployType.HYPERION,
                        'product_type': ProductType.FATE,
                        'create_time': current_timestamp(),
                        'update_time': current_timestamp()
                    }
                    DBOperator.create_entity(DeployJob, deploy_job)

                DBOperator.create_entity(DeploySite, deploy_site)
                site_info = {
                    'party_id': deploy_site.get('party_id'),
                    'status': SiteStatus.JOINED
                }
                data = {
                    'service_status': ServiceStatus.UNAVAILABLE
                }
                DBOperator.update(FateSiteInfo, data, site_info)

            return 0, "Connect success."
        else:
            return 100, "Connect failed."
    else:
        return 100, "Connect failed."


def do_test_only(party_id):
    deploy_site = {
        'party_id': party_id,
        'product_type': ProductType.FATE,
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component = {
        'party_id': party_id,
        'component_name': 'fateflow',
        'product_type': ProductType.FATE,
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component_list = get_deploy_component(deploy_component)
    if deploy_component_list:
        address = deploy_component_list[0].address.split(':')
        if len(address) == 2:
            test_req = {
                'guest_party_id': party_id,
                'host_party_id': TEST_PARTY_ID,
                'ip': address[0],
                'work_mode': WORK_MODE
            }

            req_url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('AutoTestUri', '') + '/toy'
            resp = requests.post(url=req_url, json=test_req)
            if resp.status_code == 200:
                resp_info = resp.json()
                if resp_info.get('code', 100) == 0:
                    data = {}
                    data['toy_test_only'] = TestStatus.TESTING
                    data['toy_test_only_read'] = ToyTestOnlyTypeRead.YES
                    DBOperator.update_entity(DeploySite, data)


def auto_test(request_data):
    test_list = get_auto_test({'party_id': request_data.get('partyId')})
    test_value_map = {'fate': True}
    for test_item in test_list:
        test_value = True
        if test_item.status != TestStatus.YES:
            test_value = False
        if test_item.test_item in ['clustermanager', 'mysql', 'nodemanager', 'fateflow', 'rollsite', 'fateboard']:
            if not test_value:
                test_value_map["fate"] = test_value
        else:
            test_value_map[test_item.test_item] = test_value

    if request_data.get("ifOnly"):
        do_test_only(request_data.get('partyId'))
    elif not request_data.get("fate"):
        data = {}
        data['status'] = TestStatus.WAITING
        data['start_time'] = current_timestamp()
        req_body = connect_hyperion(request_data.get('partyId'))
        url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('AutoTestUri') + "/status"
        resp = requests.post(url=url, json=req_body)
        if resp.status_code != 200:
            # TODO log error
            return 100, resp.text, {}
        resp_dict = resp.json()
        toy_test = True
        if resp_dict.get('retcode') == 0:
            for item in resp_dict.get('data', []):
                data['end_time'] = current_timestamp()
                auto_test_info = {
                    'party_id': request_data.get('partyId'),
                    'test_item': item.get('name')
                }
                deploy_data = {}
                if item.get('status') == 'running':
                    data['status'] = TestStatus.YES
                    deploy_data['deploy_status'] = DeployStatus.IN_TESTING
                else:
                    data['status'] = DeployStatus.TEST_FAILED
                    deploy_data['deploy_status'] = DeployStatus.TEST_FAILED
                    toy_test = False
                deploy_component = {
                    'party_id': request_data.get('partyId'),
                    'product_type': ProductType.FATE,
                    'component_name': item.get('name'),
                    'deploy_type': DeployType.HYPERION,
                    'is_valid': IsValid.YES
                }
                DBOperator.update(AutoTest, auto_test_info, data)
                DBOperator.update(DeployComponent, deploy_component, deploy_data)

                deploy_site = {
                    'party_id': request_data.get('partyId'),
                    'product_type': ProductType.FATE,
                    'deploy_type': DeployType.HYPERION,
                    'is_valid': IsValid.YES
                }
                if toy_test:
                    do_test({'party_id': request_data.get('partyId')}, 'single')
                else:
                    deploy_site_info = {
                        'single_test': TestStatus.NO,
                        'toy_test': TestStatus.NO,
                        'minimize_fast_test': TestStatus.NO,
                        'minimize_normal_test': TestStatus.NO,
                        'deploy_status': DeployStatus.TEST_FAILED
                    }
                    DBOperator.update(DeploySite, deploy_site, deploy_site_info)

                    auto_test_info['test_item'] = ''
                    auto_test_info['party_id'] = request_data.get('partyId')
                    DBOperator.update_entity(AutoTest, {'status': DeployStatus.TEST_FAILED})
            return 0, 'success', {}
        else:
            deploy_data = {}
            deploy_data['deploy_status'] = DeployStatus.TEST_FAILED
            data['status'] = TestStatus.NO
            deploy_component = {
                'party_id': request_data.get('partyId'),
                'product_type': ProductType.FATE,
                'deploy_type': DeployType.HYPERION,
                'is_valid': IsValid.YES
            }
            auto_test_info = {
                'party_id': request_data.get('partyId')
            }
            DBOperator.update(AutoTest, auto_test_info, data)
            DBOperator.update(DeployComponent, deploy_component, deploy_data)
            return 100, 'failed', {}

    elif not test_value_map.get('Single Test'):
        do_test({'party_id': request_data.get('partyId')}, 'single')
    elif not test_value_map.get('Toy Test'):
        do_test({'party_id': request_data.get('partyId')}, 'toy')
    elif not test_value_map.get('Minimize Fast Test'):
        do_test({'party_id': request_data.get('partyId')}, 'fast')
    elif not test_value_map.get('Minimize Normal Test'):
        do_test({'party_id': request_data.get('partyId')}, 'normal')
    return 0, 'success', {}


def do_test(auto_test_info: dict, test_item: str):
    deploy_site = {
        'party_id': auto_test_info.get('party_id'),
        'product_type': ProductType.FATE,
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component = {
        'party_id': auto_test_info.get('party_id'),
        'component_name': 'fateflow',
        'product_type': ProductType.FATE,
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component_list = get_component_list(deploy_component)
    data = {}
    if deploy_component_list:
        address = deploy_component_list[0].get('address', '').split(':')
        if len(address) == 2:
            single_test_req = {
                'party_id': auto_test_info.get('party_id'),
                'ip': address[0]
            }

            test_req = {
                'guest_party_id': auto_test_info.get('party_id'),
                'host_party_id': TEST_PARTY_ID,
                'ip': address[0],
                'work_mode': WORK_MODE
            }

            min_req = {
                'arbiter_party_id': TEST_PARTY_ID,
                'guest_party_id': deploy_site.get('party_id'),
                'host_party_id': TEST_PARTY_ID,
                'ip': address[0]
            }

            if test_item == 'single':
                url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('AutoTestUri') + '/' + test_item
                resp = requests.post(url, json=single_test_req)
            elif test_item == 'toy':
                url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('AutoTestUri') + '/' + test_item
                resp = requests.post(url, json=test_req)
            elif test_item == 'fast' or test_item == 'normal':
                url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('AutoTestUri') + '/' + test_item
                resp = requests.post(url, json=min_req)
            else:
                resp = {'retcode': 100, 'retmsg': f'invalid test item: {test_item}'}

            if isinstance(resp, dict):
                return resp
            else:
                if resp.status_code == 200:
                    resp_info = resp.json()
                    if resp_info.get('retcode', 100) == 0:
                        if test_item == 'single':
                            data['status'] = TestStatus.TESTING
                            data['start_time'] = current_timestamp()
                            auto_test_info['test_item'] = 'Single Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            data['status'] = TestStatus.WAITING
                            auto_test_info['test_item'] = 'Toy Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = 'Minimize Fast Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'single_test': TestStatus.TESTING,
                                'toy_test': TestStatus.WAITING,
                                'minimize_fast_test': TestStatus.WAITING,
                                'minimize_normal_test': TestStatus.WAITING,
                                'deploy_status': DeployStatus.IN_TESTING
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)
                        elif test_item == 'toy':
                            data['status'] = TestStatus.TESTING
                            auto_test_info['test_item'] = 'Toy Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            data['status'] = TestStatus.WAITING
                            auto_test_info['test_item'] = "Minimize Fast Test"
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = "Minimize Normal Test"
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'toy_test': TestStatus.TESTING,
                                'minimize_fast_test': TestStatus.WAITING,
                                'minimize_normal_test': TestStatus.WAITING,
                                'deploy_status': DeployStatus.IN_TESTING
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)

                        elif test_item == 'fast':
                            data['status'] = TestStatus.TESTING
                            auto_test_info['test_item'] = 'Minimize Fast Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            data['status'] = TestStatus.WAITING
                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'minimize_fast_test': TestStatus.TESTING,
                                'minimize_normal_test': TestStatus.WAITING,
                                'deploy_status': DeployStatus.IN_TESTING
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)

                        elif test_item == 'normal':
                            data['status'] = TestStatus.TESTING
                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'minimize_normal_test': TestStatus.TESTING,
                                'deploy_status': DeployStatus.IN_TESTING
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)
                    else:
                        if test_item == 'single':
                            data['status'] = TestStatus.NO
                            data['start_time'] = current_timestamp()
                            auto_test_info['test_item'] = 'Single Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = 'Toy Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = 'Minimize Fast Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'single_test': TestStatus.NO,
                                'toy_test': TestStatus.NO,
                                'minimize_fast_test': TestStatus.NO,
                                'minimize_normal_test': TestStatus.NO,
                                'deploy_status': DeployStatus.TEST_FAILED
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)

                        elif test_item == 'toy':
                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = 'Toy Test'
                            DBOperator.update(AutoTest, data, auto_test_info)

                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = "Minimize Fast Test"
                            DBOperator.update(AutoTest, auto_test_info, data)

                            auto_test_info['test_item'] = "Minimize Normal Test"
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'toy_test': TestStatus.NO,
                                'minimize_fast_test': TestStatus.NO,
                                'minimize_normal_test': TestStatus.NO,
                                'deploy_status': DeployStatus.TEST_FAILED
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)

                        elif test_item == 'fast':
                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = 'Minimize Fast Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'minimize_fast_test': TestStatus.NO,
                                'minimize_normal_test': TestStatus.NO,
                                'deploy_status': DeployStatus.TEST_FAILED
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)

                        elif test_item == 'normal':
                            data['status'] = TestStatus.NO
                            auto_test_info['test_item'] = 'Minimize Normal Test'
                            DBOperator.update(AutoTest, auto_test_info, data)

                            query_filters = {
                                'minimize_normal_test': TestStatus.NO,
                                'deploy_status': DeployStatus.TEST_FAILED
                            }
                            DBOperator.update(DeploySite, query_filters, deploy_site)


def commit_package(request_data):
    version_list = DBOperator.query_entity(FateVersion, fate_version=request_data.get('fateVersion'))
    if version_list:
        data = {
            'fate_version': request_data.get('fateVersion'),
            'deploy_status': DeployStatus.LOADED,
            'click_type': ClickType.ACQUISITION,
            'version_index': version_list[0].to_json().get('version_index')
        }
        deploy_site_info = {
            'party_id': request_data.get('partyId'),
            'product_type': ProductType.FATE,
            'is_valid': IsValid.YES,
            'deploy_type': DeployType.HYPERION
        }
        DBOperator.update(DeploySite, deploy_site_info, data)

        component_version_list = DBOperator.query_entity(ComponentVersion, fate_version=request_data.get('fateVersion'),
                                                         product_type=ProductType.FATE)
        kubenetes_conf_list = DBOperator.query_entity(KubenetesConf, deploy_type=DeployType.HYPERION)
        component_version_map = {}
        if kubenetes_conf_list:
            for offset, instance in enumerate(component_version_list):
                instance_info = instance.to_json()
                port = get_base_config(instance_info.get('component_name'), 0)
                node_list = get_node_ip(kubenetes_conf_list[0])
                if len(node_list) < 1:
                    continue
                component_version_map[instance_info.get('component_name')] = {
                    'version': instance_info.get('component_version'),
                    'address': f'{node_list[0]}:{port}'
                }
                deploy_component_info = {
                    'party_id': request_data.get('partyId'),
                    'component_name': instance_info.get('component_name'),
                    'product_type': ProductType.FATE,
                    'deploy_type': DeployType.HYPERION,
                    'is_valid': IsValid.YES
                }
                deploy_component_list = get_component_list(deploy_component_info)
                if len(deploy_component_list) == 0:
                    deploy_component_info['fate_version'] = request_data.get('fateVersion')
                    deploy_component_info['component_version'] = instance_info.get('component_version')
                    deploy_component_info['component_name'] = instance_info.get('component_name')
                    deploy_component_info['address'] = component_version_map[instance_info.get('component_name')].get('address')
                    deploy_component_info['version_index'] = instance_info.get('version_index')
                    deploy_component_info['deploy_status'] = DeployStatus.LOADED
                    DBOperator.create_entity(DeployComponent, deploy_component_info)
                else:
                    data = {
                        'fate_version': component_version_list[offset],
                        'address': node_list[0] + ':' + int(port),
                        'component_version': component_version_list[offset].get('component_version'),
                        'version_index': component_version_list[offset].get('version_index'),
                    }
                    DBOperator.update(DeployComponent, deploy_component_info, data)
    return 0, 'success', {}


def get_test_list(request_data):
    deploy_site_list = DBOperator.query_entity(DeploySite, party_id=request_data.get('partyId'),
                                               product_type=request_data.get('productType'),
                                               deploy_type=DeployType.HYPERION,
                                               is_valid=IsValid.YES)
    if deploy_site_list:
        fate_version = deploy_site_list[0].fate_version
        auto_test_list = DBOperator.query_entity(AutoTest, party_id=request_data.get('partyId'),
                                                 product_type=request_data.get('productType'),
                                                 fate_version=fate_version)
        data = {}
        for item in auto_test_list:
            auto_test_item = {
                'testItem': item.test_item,
                'duration': item.end_time - item.start_time,
                'status': {
                    'code': item.status,
                    'desc': TestStatus.to_str(item.status)
                }
            }
            if item.status == TestStatus.TESTING:
                auto_test_item['duration'] = -1

            if item.test_item in [TestItem.to_str(status_code) for status_code in [TestItem.SINGLE, TestItem.NORMAL, TestItem.FAST, TestItem.TOY]]:
                data[item.test_item] = [auto_test_item]
            else:
                if TestItem.to_str(TestItem.POD) not in data:
                    data[TestItem.to_str(TestItem.POD)] = []
                else:
                    data[TestItem.to_str(TestItem.POD)].append(auto_test_item)
        resp = {'AutoTest': data}
        return 0, 'success', resp
    return 100, 'failed, no deploy site list found', {}


def get_log(request_data):
    req_url = k8s_service.get_kubenetes_url(DeployType.HYPERION)
    resp = requests.post(url=f'{req_url}{HYPERION_SETTINGS.get("LogUri")}', json=request_data)
    if resp.status_code == 200:
        return 0, 'success', {'content': resp.json(), 'total': len(resp.json())}
    # TODO logger.error()
    return 100, 'get server log failed', {'content': [], 'total': 0}


def auto_acquire(request_data):
    instances = DBOperator.query_entity(KubenetesConf, deploy_type=DeployType.HYPERION)
    if not instances:
        return 100, 'not found'
    instance = instances[0].to_json()
    version_instance = DBOperator.query_entity(FateVersion, fate_version=request_data.get('fateVersion'))
    if not version_instance:
        return 100, 'not found'
    version_instance = version_instance[0].to_json()
    data = {
        'fate_version': request_data.get('fateVersion'),
    }
    if version_instance.get('package_status', 0) == PackageStatus.NO:
        json_data = {
            "version": request_data.get('fateVersion'),
            "url": version_instance.get('package_url')
        }
        resp = requests.post(url=f"{instance.get('kubenetes_url')}{HYPERION_SETTINGS.get('PackageDownUri')}",
                             json=json_data)
        if resp.status_code == 200:
            data['deploy_status'] = DeployStatus.LOADING
            DBOperator.update_entity(DeploySite, data)
            return 0, 'success', data
        else:
            data['deploy_status'] = DeployStatus.LOAD_FAILED
            DBOperator.update_entity(DeploySite, data)
            # TODO log
            return 100, 'download failed', data
    elif version_instance.get('package_status', 0) == PackageStatus.YES:
        data['deploy_status'] = DeployStatus.LOADED
    elif version_instance.get('package_status', 0) == PackageStatus.PULLING:
        data['deploy_status'] = DeployStatus.LOADING
    elif version_instance.get('package_status', 0) == PackageStatus.FAILED:
        data['deploy_status'] = DeployStatus.LOAD_FAILED
    DBOperator.update_entity(DeploySite, data)
    return 0, 'success', data


def local_upload(request_data):
    conf = get_kubenetes_conf(DeployType.HYPERION)
    if conf.get('id') == 0:
        return 100, 'no kubenetes conf found', {}

    req = {
        'party_id': request_data.get('partyId'),
        'ip': request_data.get('ip'),
        'path': request_data.get('path')
    }
    url = conf.get('kubenetes_url', '') + HYPERION_SETTINGS.get('LocalUploadUri')
    resp = requests.post(url=url, json=req)
    if resp.status_code != 200:
        return 100, 'connect hyperion api failed', {}
    else:
        conn_resp = resp.json()
        deploy_site = {
            'party_id': request_data.get('partyId'),
            'is_valid': IsValid.YES,
            'deploy_type': DeployType.HYPERION
        }
        if conn_resp.get('retcode') != 0:
            data = {
                'deploy_status': DeployStatus.LOAD_FAILED
            }
            DBOperator.update(DeploySite, deploy_site, data)
            return 100, f'connect hyperion api failed, info: {conn_resp.get("retmsg")}', {}
        else:
            data = {
                'deploy_status': DeployStatus.LOADED,
                'fate_version': conn_resp.get('data', {}).get('fate_version'),
            }
            DBOperator.update(DeploySite, deploy_site, data)
            return 0, 'upload success', {}


def get_install_component_list(request_data):
    deploy_component = {
        'federated_id': request_data.get('federatedId'),
        'party_id': request_data.get('partyId'),
        'product_type': request_data.get('product_type'),
        'is_valid': IsValid.YES
    }

    deploy_component_list = get_deploy_component(deploy_component)
    if not deploy_component_list:
        return 0, 'no deploy component data found', []

    data = []
    for component in deploy_component_list:
        data.append({
            'component_name': component.get('component_name'),
            'address': component.get('address'),
            'deploy_status': {
                'code': component.get('deploy_status'),
                'desc': DeployStatus.to_str(component.get('deploy_status'))
            },
            'duration': component.get('duration')
        })

    return 0, 'success', data


def update(request_data):
    if len(request_data.get('componentName', [])) == 0:
        return 100, 'no components to be updated', {}
    deploy_component = {
        'faderated_id': request_data.get('federatedId'),
        'party_id': request_data.get('partyId'),
        'product_type': ProductType.FATE,
        'component_name': request_data.get('componentName'),
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component_list = get_deploy_component(deploy_component)
    if not deploy_component_list:
        return 100, 'no component data found', {}
    if deploy_component_list[0].get('deploy_status') in [DeployStatus.LOADED, DeployStatus.INSTALLED,
                                                         DeployStatus.UNDER_INSTALLATION, DeployStatus.IN_TESTING,
                                                         DeployStatus.TEST_FAILED, DeployStatus.IN_TESTING,
                                                         DeployStatus.INSTALLED_FAILED, DeployStatus.TEST_PASSED]:
        tag = k8s_service.check_node_ip(request_data, DeployType.HYPERION)
        if not tag:
            return 100, 'ip not correct', {}

        data = {
            'address': request_data.get('address')
        }
        DBOperator.update(DeployComponent, deploy_component, data)
        data = {
            'click_type': ClickType.ACQUISITION
        }
        deploy_site = {
        'faderated_id': request_data.get('federatedId'),
        'party_id': request_data.get('partyId'),
        'product_type': ProductType.FATE,
        'is_valid': IsValid.YES
        }
        DBOperator.update(DeploySite, deploy_site, data)
    return 0, 'success', {}


def click(request_data):
    conf = get_kubenetes_conf(DeployType.HYPERION)
    if request_data.get('clickType') in [ClickType.PREPARE, ClickType.SYSTEM_CHECK, ClickType.INSTALL]:
        if conf.get('click_type') < request_data.get('clickType'):
            data = {
                'click_type': request_data.get('clickType')
            }
            DBOperator.update(KubenetesConf, conf, data)

            deploy_site = {
                'is_valid': IsValid.YES,
                'deploy_type': DeployType.HYPERION
            }
            deploy_site_list = DBOperator.query_entity(DeploySite, deploy_site)
            for site in deploy_site_list:
                if site.get('click_type') < request_data.get('clickType'):
                    DBOperator.update(DeploySite, deploy_site, data)
            return 0, 'success', {}
        return 100, 'failed', {}

    deploy_site = {
        'federated_id': request_data.get('federatedId'),
        'party_id': request_data.get('partyId'),
        'product_type': request_data.get('productType'),
        'is_valid': IsValid.YES
    }
    deploy_site_list = DBOperator.query_entity(DeploySite, deploy_site)

    if not deploy_site_list:
        if conf.get('id') > 0:
            deploy_site = {
                'party_id': request_data.get('partyId'),
                'product_type': ProductType.FATE,
                'status': SiteRunStatus.UNKNOWN,
                'click_type': ClickType.CONNECT,
                'kubenetes_id': conf.get('id'),
                'deploy_status': DeployStatus.UNKNOWN,
                'single_test': TestStatus.WAITING,
                'toy_test': TestStatus.WAITING,
                'minimize_normal_test': TestStatus.WAITING,
                'minimize_fast_test': TestStatus.WAITING,
                'toy_test_only': ToyTestOnly.NO_TEST,
                'toy_test_only_read': ToyTestOnlyRead.YES,
                'deploy_type': DeployType.HYPERION,
                'is_valid': IsValid.YES,
            }
            if conf.get('click_type') > 0:
                deploy_site['click_type'] = conf.get('click_type')

            deploy_site_list = DBOperator.query_entity(DeploySite, deploy_site)
            if not deploy_site_list:
                DBOperator.create_entity(DeploySite, deploy_site)
            return 0, 'success', {}
        return 100, 'failed', {}

    if deploy_site_list[0].get('click_type') <= request_data.get('clickType'):
        data = {
            'click_type': request_data.get('clickType')
        }
        DBOperator.update(DeploySite, deploy_site, data)

    if request_data.get('clickType') == ClickType.TEST:
        deploy_component = {
            'federated_id': request_data.get('federatedId'),
            'party_id': request_data.get('partyId'),
            'product_type': request_data.get('productType'),
            'is_valid': IsValid.YES
        }

        data = {
            'duration': current_timestamp() - deploy_site_list[0].get('create_time'),
            'finish_time': current_timestamp(),
            'deploy_status': DeployStatus.SUCCESS,
            'status': SiteRunStatus.RUNNING
        }

        DBOperator.update(DeployComponent, deploy_component, data)

        deploy_site = {
            'federated_id': request_data.get('federatedId'),
            'party_id': request_data.get('partyId'),
            'product_type': request_data.get('productType'),
            'is_valid': IsValid.YES
        }
        DBOperator.update(DeploySite, deploy_site, data)

        site_info = {
            'party_id': request_data.get('partyId'),
        }

        data = {
            'federated_id': request_data.get('federatedId'),
            'service_status': ServiceStatus.AVAILABLE
        }
        DBOperator.update(FateSiteInfo, site_info, data)
    return 0, 'success', {}


def install(request_data):
    site = {
        'party_id': request_data.get('partyId'),
        'status': SiteStatus.JOINED
    }

    site_list = DBOperator.query_entity(FateSiteInfo, **site)
    if not site_list:
        return 100, 'no sites found', {}

    deploy_site = {
        'federated_id': request_data.get('federatedId'),
        'party_id': request_data.get('partyId'),
        'product_type': request_data.get('productType'),
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_site_list = DBOperator.query_entity(DeploySite, **deploy_site)

    if not deploy_site_list:
        return 100, 'no deploy site found', {}
    else:
        if deploy_site_list[0].get('deploy_status') in [DeployStatus.UNDER_INSTALLATION, DeployStatus.INSTALLING]:
            return 100, 'party is installing or already installed', {}

    deploy_component = {
        'party_id': request_data.get('partyId'),
        'product_type': request_data.get('productType'),
        'deploy_type': DeployType.HYPERION,
        'is_valid': IsValid.YES
    }

    deploy_component_list = DBOperator.query_entity(DeployComponent, **deploy_component)
    req = {
        'party_id': request_data.get('partyId'),
        'fate_version': deploy_site_list[0].get('fate_version'),
        'role': RoleType.to_str(site_list[0].get('role'))
    }

    modules = []
    for item in deploy_component_list:
        modules.append(item.get('component_name'))
        arr1 = item.get('address').split(',')
        address = []
        for v in arr1:
            arr2 = v.split(':')
            port = int(arr2[1])
            address.append(arr2[0])

            ip_node = {
                'ip': address,
                'port': port
            }

            java = {
                'ip': address
            }

            if item.get('component_name') == 'mysql':
                req['modules']['mysql'] = {
                    'ip_node': ip_node,
                    'password': 'fate_pass',
                    'user': 'fate_user'
                }
            elif item.get('component_name') == 'clustermanager':
                req['modules']['clustermanager'] = ip_node
            elif item.get('component_name') == 'nodemanager':
                req['modules']['nodemanger'] = ip_node
            elif item.get('component_name') == 'fateflow':
                req['modules']['flow'] = {
                    'ip': address,
                    'dbname': 'fate_flow',
                    'grpc_port': 9360,
                    'http_port': port
                }
                req['modules']['python'] = {
                    'ip': address
                }

            elif item.get('component_name') == 'fateboard':
                req['modules']['fateboard'] = {
                    'dbname': 'fate_flow',
                    'ip_node': ip_node
                }
                req['modules']['java'] = {
                            'ip': ip_node['ip'],
                            'java': {
                                'ip': address
                            }
                        }
                req['modules']['supervisor'] = {
                    'ip': address
                }

            elif item.get('component_name') == 'rollsite':
                req['modules']['rollsite'] = {
                    'ip_node': ip_node,
                    'port': port,
                    'default_rules': [{
                        'name': 'default',
                        'ip': DEPLOY_SETTINGS.get('EXCHANGE_IP', ""),
                        "port": DEPLOY_SETTINGS.get('EXCHANGE_PORT', 0),
                    }],
                    'rules': [{
                        'name': 'default',
                        'ip': address[0],
                        "port": port,
                    },
                        {
                            'name': 'fateflow',
                            'ip': address[0],
                            "port": 9360,
                        }],
                }
                req['modules']['eggroll'] = {
                    'ip': address,
                    'dbname': 'eggroll_meta',
                    'egg': DEPLOY_SETTINGS.get('SESSION_PROCESSOR_PER_NODE', 0)
                }

    url = k8s_service.get_kubenetes_url(DeployType.HYPERION) + HYPERION_SETTINGS.get('JobSubmitUri')
    resp = requests.post(url=url, json=req)
    data = {}
    if resp.status_code == 200:
        conn_resp = resp.json()
        if conn_resp.get('retcode') == 0:
            data['deploy_status'] = DeployStatus.UNDER_INSTALLATION
            data['job_id'] = conn_resp.get('data', {}).get('job_id')
            DBOperator.update(DeployComponent, deploy_component, data)
            data['config'] = json.dumps(req)
            DBOperator.update(DeploySite, deploy_site, data)

            deploy_job = {
                'job_id': conn_resp.get('data', {}).get('job_id'),
                'job_type': JobType.INSTALL,
                'status': JobStatus.RUNNING,
                'party_id': req.get('party_id'),
                'deploy_type': DeployType.HYPERION,
                'product_type': ProductType.FATE
            }
            DBOperator.create_entity(DeployJob, deploy_job)
            return 0, 'submit success', {}
        return 100, f'submit failed, details: {conn_resp.get("retmsg")}', {}
    return 100, f'submit failed, details: {resp.text}', {}

