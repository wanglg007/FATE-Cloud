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
from fate_manager.service import monitor_service

manager = Flask(__name__)


@manager.errorhandler(500)
def internal_server_error(e):
    stat_logger.exception(e)
    return get_json_result(retcode=100, retmsg=str(e))


@manager.route('/total', methods=['POST'])
def get_total_details():
    request_data = request.json
    require_parameters = ['startDate', 'endDate', 'pageNum', 'pageSize']
    check_config(request_data, require_parameters)
    retcode, retmsg, data = monitor_service.get_monitor_total(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('/institution', methods=['POST'])
def institution():
    request_data = request.json
    # require_parameters = ['FederatedSite', 'productType']
    require_parameters = ['startDate', 'endDate', 'pageNum', 'pageSize']

    retcode, retmsg, data = monitor_service.get_institution_base_statics(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)


@manager.route('/site', methods=['POST'])
def site():
    request_data = request.json
    # require_parameters = ['FederatedSite', 'productType']
    require_parameters = ['startDate', 'endDate', 'pageNum', 'pageSize']

    retcode, retmsg, data = monitor_service.get_site_base_statics(request_data)
    return get_json_result(retcode=retcode, retmsg=retmsg, data=data)