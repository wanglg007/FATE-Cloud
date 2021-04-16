from db.db_models import DeployComponent
from fate_manager.entity.types import (ProductType, IsValid, DeployType, PackageStatus, DeployStatus, ClickType)
import random

from operation.db_operator import DBOperator


def get_node_ip(kubenete_instance):
    kubenete_info = kubenete_instance.to_json()
    node = []
    if kubenete_info.get('node_list'):
        node_list = kubenete_info.get('node_list').split(',')
        if kubenete_info.get('deploy_type') == DeployType.KUBEFATE:
            if len(node_list) > 0:
                node = node_list[random.randint(1, len(node_list))]
                node = node.split(':')
        else:
            node = node_list
    return node


def get_kubenetes_url(deploy_type):
    sql = 'SELECT t1.id t1.kubenetes_url, t1.node_list ' \
          'FROM t_fate_kubenetes_conf t1 ' \
          f'JOIN t_fate_deploy_site t2 ON t1.id = t2.kubenetes_id and t2.is_valid = 1 and t1.deploy_type={deploy_type} '
    res = DBOperator.query_with_raw_sql(sql)
    if res:
        return res[0]
    return {}


def check_node_ip(request_data, deploy_type):
    kubenetes_conf = get_kubenetes_url(DeployType.HYPERION)
    address_list = request_data.get('address', '').split(',')
    tag = False
    for address in address_list:
        deploy_component = {
            'party_id': request_data.get('partyId'),
            'is_valid': IsValid.YES,
            'address': request_data.get('address')
        }
        deploy_component_list = DBOperator.query_entity(DeployComponent, deploy_component)
        if not deploy_component_list:
            tag = False
            break

        ip_list = address.split(':')
        if len(ip_list) != 2:
            tag = False
            break
        elif len(ip_list[1]) == 0:
            tag = False
            break

        node_list = kubenetes_conf.get('node_list', '').split(':')
        if deploy_type == DeployType.KUBEFATE:
            for node in node_list:
                lab_list = node.split(':')
                if len(lab_list) == 2:
                    if lab_list[1] == ip_list[0]:
                        tag = True
                        break
        else:
            for node in node_list:
                if node == ip_list[0]:
                    tag = True
                    break
    return tag

