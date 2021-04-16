#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import Flask, request
from fate_manager.settings import HYPERION_SETTINGS
from fate_manager.utils.api_utils import get_json_result
from fate_manager.db.db_models import (DeployPrepare, KubenetesConf, FateVersion, DeploySite,
                                       AutoTest)
from fate_manager.operation.db_operator import DBOperator
from fate_manager.entity.types import DeployType, PackageStatus, DeployStatus, ProductType, IsValid
import requests
from fate_manager.settings import stat_logger
from fate_manager.utils.conf_utils import check_config
from fate_manager.service import hyperion_service

manager = Flask(__name__)


@manager.errorhandler(500)
def internal_server_error(e):
    stat_logger.exception(e)
    return get_json_result(retcode=100, retmsg=str(e))


@manager.route('commit', methods=['POST'])
def commit():
    request_data = request.json
    require_parameters = ['deployType', 'fateVersion', 'federatedId', 'partyId', 'productType']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.commit_package(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('install', methods=['POST'])
def install():
    request_data = request.json
    require_parameters = ['federatedId', 'partyId', 'productType']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.install(request_data)
    return get_json_result()


@manager.route('upgrade', methods=['POST'])
def upgrade():
    # TODO to be completed
    request_data = request.json
    return get_json_result()


@manager.route('click', methods=['POST'])
def click():
    request_data = request.json
    require_parameters = ['federatedId', 'partyId', 'productType', 'clickType']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.click(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('update', methods=['POST'])
def update():
    request_data = request.json
    require_parameters = ['partyId', 'productType', 'federatedId', 'componentName', 'address']
    check_config(request_data, require_parameters)
    retcode, retmsg = hyperion_service.update(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg)


@manager.route('/connecthyperion')
def connect_hyperion():
    request_data = request.json
    require_parameters = ['ansibleUrl', 'partyId']
    check_config(request_data, require_parameters)
    retcode, retmsg = hyperion_service.connect_hyperion(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg)


@manager.route('/autoacuqire', methods=['POST'])
def auto_acuqire():
    request_data = request.json
    require_parameters = ['fateVersion', 'partyId', 'url']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.auto_acquire(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('upload', methods=['POST'])
def upload():
    request_data = request.json
    require_parameters = ['path', 'partyId', 'ip', 'siteName']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.local_upload(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('componentlist', methods=['POST'])
def component_list():
    request_data = request.json
    require_parameters = ['ifOnly', 'partyId', 'productType']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.get_component_list(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('installlist', methods=['POST'])
def install_list():
    request_data = request.json
    require_parameters = ['partyId', 'productType', 'federatedId']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.get_install_component_list(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('autotest', methods=['POST'])
def auto_test():
    request_data = request.json
    require_parameters = ['partyId', 'productType', 'ifOnly']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.auto_test(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('testlist', methods=['POST'])
def test_list():
    request_data = request.json
    require_parameters = ['partyId', 'siteName', 'productType']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.get_test_list(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('log', methods=['POST'])
def log():
    request_data = request.json
    require_parameters = ['level']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = hyperion_service.get_log(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)