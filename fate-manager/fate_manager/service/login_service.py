import base64
import hmac
import json

from fate_manager.utils.base_utils import current_timestamp
from fate_manager.db.db_models import AccountInfo, FateUserInfo, FederatedInfo, TokenInfo,FateSiteInfo
from fate_manager.entity.status_code import UserStatusCode,InstitutionStatusCode
from fate_manager.entity.types import UserRole, ActivateStatus, PermissionType, IsValidType
from fate_manager.operation.db_operator import DBOperator
from fate_manager.settings import EXPIRE_TIME
from fate_manager.settings import login_service_logger as logger
from fate_manager.utils.model_utils import transform_dict_key
from fate_manager.utils.request_cloud_utils import request_cloud_manager,request_cloud_manager_active


def fate_manager_activate(request_data):
    logger.info(f'request data: {request_data}')
    user_name = request_data.get("userName")
    accounts = DBOperator.query_entity(AccountInfo, role=UserRole.ADMIN)
    # if accounts:
    #     raise Exception(UserStatusCode.NoFoundAccount, f"activate failed: fate manager has been activated")
    users = DBOperator.query_entity(FateUserInfo, user_name=user_name)
    if not users:
        raise Exception(UserStatusCode.NoFoundUser, f"user {user_name} no found ")

    # DBOperator.update_entity(FateUserInfo, {"user_name": user_name, "is_delete": 0})

    institutions = request_data.get('institutions')
    institution = DBOperator.query_entity(FateSiteInfo, institutions=institutions)
    if institution:
        raise Exception(InstitutionStatusCode.Institution_Not_Allow_Activate,
                        f"Institution has exist {institutions} actived record,not allow activate ")

    body = {"registrationLink": request_data.get("link")}
    logger.info(f'start request cloud: body {body}')
    res = request_cloud_manager_active(uri_key="UserActivate", data=request_data, body=body,
                                            url=request_data.get("federatedUrl"))
    logger.info(f'response from cloud for institution info: {res}')

    # save account info
    request_info = transform_dict_key(res)
    saveAccountInfo = {}
    saveAccountInfo["creator"] = user_name
    saveAccountInfo["permission_list"] = [PermissionType.BASIC, PermissionType.DEPLOY,
                                           PermissionType.FATEBOARD, PermissionType.FATESTUDIO]
    saveAccountInfo["role"] = UserRole.ADMIN
    saveAccountInfo["status"] = IsValidType.YES
    saveAccountInfo["cloud_user"] = 1

    saveAccountInfo["active_url"] = request_data.get("federatedUrl")
    saveAccountInfo["institutions"] = request_data.get("institutions")
    saveAccountInfo["fate_manager_id"] = request_data.get("fateManagerId")
    saveAccountInfo["user_name"] = user_name

    data = request_info.get('fate_manager_user').get('secretInfo')
    data_dct = json.loads(data)
    saveAccountInfo["app_secret"] = data_dct.get("secret")
    saveAccountInfo["app_key"] = data_dct.get("key")

    logger.info(f'create account info: {saveAccountInfo}')
    DBOperator.safe_save(AccountInfo, saveAccountInfo)

    # save federated info
    saveFederatedInfo = {}
    federated_info = request_info.get('federated_organization')
    federated_data = transform_dict_key(federated_info)
    saveFederatedInfo["institutions"] = request_data.get('institutions')
    saveFederatedInfo["federated_url"] = request_data.get("federatedUrl")
    saveFederatedInfo["status"] = 1
    saveFederatedInfo["federated_id"] = federated_data.get('id')
    saveFederatedInfo["institution"] = federated_data.get('institution')
    saveFederatedInfo["federated_organization"] = federated_data.get('name')
    saveFederatedInfo["federated_organization_create_time"] = federated_data["create_time"]
    logger.info(f'save federated info {saveFederatedInfo}')
    DBOperator.safe_save(FederatedInfo, saveFederatedInfo)
    return res


def fate_manager_login(request_data):
    user_name = request_data.get("userName")
    password = request_data.get("passWord")
    accounts = DBOperator.query_entity(AccountInfo, status=ActivateStatus.YES, user_name=user_name)
    if not accounts:
        raise Exception(UserStatusCode.NoFoundAccount, f"no found account by username:{user_name}")
    account = accounts[0]
    if account.role not in [UserRole.ADMIN, UserRole.DEVELOPER] :
        raise Exception(UserStatusCode.AccountRoleLow, f"user {user_name} is not allowed to login")
    users = DBOperator.query_entity(FateUserInfo, user_name=user_name, password=password)
    if not users:
        raise Exception(UserStatusCode.LoginFailed, f"login failed:user name or password error")
    user = users[0]
    token = generate_token(user.user_name, user.password)
    token_info = {
        "user_name": user.user_name,
        "token": token,
        "expire_time": current_timestamp() + EXPIRE_TIME
    }
    DBOperator.safe_save(TokenInfo, token_info)
    return token


def fate_manager_logout(request_data, token):
    user_name = request_data.get("userName")
    accounts = DBOperator.query_entity(AccountInfo, status=ActivateStatus.YES, user_name=user_name)
    if not accounts:
        raise Exception(UserStatusCode.NoFoundAccount, f"no found account by username:{user_name}")
    logger.info(f'login out, user name: {user_name}, token :{token}')
    token_info = DBOperator.query_entity(TokenInfo, user_name=user_name, token=token)
    if not token_info:
        return False
    token_info = {
        "user_name": user_name,
        "token": token
    }
    DBOperator.delete_entity(TokenInfo, **token_info)


def fate_manager_checkjwt(request_data):
    token = request_data.get("token")
    token_info_list = DBOperator.query_entity(TokenInfo, token=token)
    if not token_info_list:
        raise Exception(UserStatusCode.NoFoundToken, "login failed: token no found")
    token_info = token_info_list[0]
    if current_timestamp() > token_info.expire_time:
        raise Exception(UserStatusCode.TokenExpired, "token expired")
    accounts = DBOperator.query_entity(AccountInfo, status=ActivateStatus.YES, user_name=token_info.user_name)
    if not accounts:
        raise Exception(UserStatusCode.NoFoundAccount, "no found account")
    account = accounts[0]
    token_info = {
        "user_name": account.user_name,
        "token": token,
        "expire_time": current_timestamp() + EXPIRE_TIME
    }
    DBOperator.safe_save(TokenInfo, token_info)
    return {"userName": account.user_name, "Institutions": account.institutions}


def generate_token(user_name, password):
    value = '\n'.join([password, str(current_timestamp())])
    sha1_key = hmac.new(user_name.encode("utf-8"), value.encode("utf-8"), 'sha1').hexdigest()
    b64_token = base64.urlsafe_b64encode(sha1_key.encode("utf-8"))
    return b64_token.decode("utf-8")
