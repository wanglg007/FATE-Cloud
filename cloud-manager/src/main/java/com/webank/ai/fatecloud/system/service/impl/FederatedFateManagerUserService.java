/*
 * Copyright 2020 The FATE Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.webank.ai.fatecloud.system.service.impl;

import com.alibaba.fastjson.JSON;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.webank.ai.fatecloud.common.Dict;
import com.webank.ai.fatecloud.common.EncryptUtil;
import com.webank.ai.fatecloud.common.util.KeyAndSecretGenerate;
import com.webank.ai.fatecloud.common.util.PageBean;
import com.webank.ai.fatecloud.system.dao.entity.FederatedFateManagerUserDo;
import com.webank.ai.fatecloud.system.dao.entity.FederatedOrganizationDo;
import com.webank.ai.fatecloud.system.dao.entity.FederatedSiteManagerDo;
import com.webank.ai.fatecloud.system.dao.mapper.FederatedFateManagerUserMapper;
import com.webank.ai.fatecloud.system.dao.mapper.FederatedOrganizationMapper;
import com.webank.ai.fatecloud.system.dao.mapper.FederatedSiteManagerMapper;
import com.webank.ai.fatecloud.system.pojo.qo.*;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.servlet.http.HttpServletRequest;
import java.io.UnsupportedEncodingException;
import java.util.*;

@Service
@Slf4j
public class FederatedFateManagerUserService {
    @Autowired
    FederatedFateManagerUserMapper federatedFateManagerUserMapper;

    @Autowired
    FederatedSiteManagerMapper federatedSiteManagerMapper;

    @Autowired
    FederatedOrganizationMapper federatedOrganizationMapper;

    @Value(value = "${server.servlet.context-path}")
    String prefix;

    public FederatedFateManagerUserDo addFateManagerUser(FateManagerUserAddQo fateManagerUserAddQo) throws UnsupportedEncodingException {
        FederatedFateManagerUserDo federatedFateManagerUserDo = new FederatedFateManagerUserDo();

        String uuid = UUID.randomUUID().toString().replace("-", "");
        federatedFateManagerUserDo.setFateManagerId(uuid);

        String institutions = fateManagerUserAddQo.getInstitutions();
        federatedFateManagerUserDo.setInstitutions(institutions);

        String appKey = KeyAndSecretGenerate.getAppKey();
        String appSecret = KeyAndSecretGenerate.getAppSecret(appKey);
        HashMap<String, String> secretMap = new HashMap<>();
        secretMap.put("key", appKey);
        secretMap.put("secret", appSecret);
        String secretInfo = JSON.toJSONString(secretMap);
        federatedFateManagerUserDo.setSecretInfo(secretInfo);


        HashMap<String, Object> stringObjectHashMap = new HashMap<>();
        stringObjectHashMap.put("fateManagerUser", federatedFateManagerUserDo);

        QueryWrapper<FederatedOrganizationDo> query = new QueryWrapper<>();
        query.select("id", "name", "institution", "create_time").eq("status", 1);
        FederatedOrganizationDo federatedOrganizationDo = federatedOrganizationMapper.selectOne(query);
        stringObjectHashMap.put("federatedOrganization", federatedOrganizationDo);

        String userInfo = JSON.toJSONString(stringObjectHashMap);
        String network = fateManagerUserAddQo.getNetwork();

        String mode = fateManagerUserAddQo.getMode();
        String fateUserRegistrationUrl = "";
        String protocol = "http://".equals(fateManagerUserAddQo.getProtocol()) ? "http://" : "https://";
        if (StringUtils.isNotBlank(mode) && "short".equals(mode)) {
            //fateUserRegistrationUrl = protocol + network + prefix + "/api/fate/user/activate" + "?st=" + institutions + "_" + uuid;
            fateUserRegistrationUrl = protocol + network + "?stl=" + institutions + "_" + uuid;
        } else {
            fateUserRegistrationUrl = protocol + network + prefix + "/api/fate/user/activate" + "?st=" + userInfo.replace("\"{", "{").replace("}\"", "}").replace("\\", "").replace("\"", "\\\"");
        }

        String encodedFateUserRegistrationUrl = EncryptUtil.encode(fateUserRegistrationUrl);

        federatedFateManagerUserDo.setRegistrationLink(encodedFateUserRegistrationUrl);

        federatedFateManagerUserDo.setCreator(fateManagerUserAddQo.getCreator());

        federatedFateManagerUserDo.setProtocol(fateManagerUserAddQo.getProtocol());
        federatedFateManagerUserDo.setNetwork(network);

        federatedFateManagerUserMapper.insert(federatedFateManagerUserDo);

        return federatedFateManagerUserDo;

    }


    public FederatedFateManagerUserDo updateFateManagerUser(FateManagerUserUpdateQo fateManagerUserUpdateQo) throws UnsupportedEncodingException {
        String institution = fateManagerUserUpdateQo.getInstitution();
        String fateManagerId = fateManagerUserUpdateQo.getFateManagerId();
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", fateManagerId);
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);
        if (federatedFateManagerUserDos.size() <= 0) {
            return null;
        }
        FederatedFateManagerUserDo federatedFateManagerUserDoOld = federatedFateManagerUserDos.get(0);

        FederatedFateManagerUserDo federatedFateManagerUserDo = new FederatedFateManagerUserDo();
        federatedFateManagerUserDo.setFateManagerId(fateManagerId);
        federatedFateManagerUserDo.setInstitutions(institution);
        federatedFateManagerUserDo.setSecretInfo(federatedFateManagerUserDoOld.getSecretInfo());

        HashMap<String, Object> stringObjectHashMap = new HashMap<>();
        stringObjectHashMap.put("fateManagerUser", federatedFateManagerUserDo);

        QueryWrapper<FederatedOrganizationDo> query = new QueryWrapper<>();
        query.select("id", "name", "institution", "create_time").eq("status", 1);
        FederatedOrganizationDo federatedOrganizationDo = federatedOrganizationMapper.selectOne(query);
        stringObjectHashMap.put("federatedOrganization", federatedOrganizationDo);

        String userInfo = JSON.toJSONString(stringObjectHashMap);
        String network = fateManagerUserUpdateQo.getNetwork();

        String fateUserRegistrationUrl = "";
        String mode = fateManagerUserUpdateQo.getMode();
        String protocol = "http://".equals(fateManagerUserUpdateQo.getProtocol()) ? "http://" : "https://";
        if (StringUtils.isNotBlank(mode) && "short".equals(mode)) {
            fateUserRegistrationUrl = protocol + network + "?stl=" + institution + "_" + fateManagerId;
        } else {
            fateUserRegistrationUrl = protocol + network + prefix + "/api/fate/user/activate" + "?st=" + userInfo.replace("\"{", "{").replace("}\"", "}").replace("\\", "").replace("\"", "\\\"");
        }

        String encodedFateUserRegistrationUrl = EncryptUtil.encode(fateUserRegistrationUrl);

        federatedFateManagerUserDoOld.setRegistrationLink(encodedFateUserRegistrationUrl);

        federatedFateManagerUserDoOld.setCreator(fateManagerUserUpdateQo.getCreator());

        federatedFateManagerUserDoOld.setProtocol(fateManagerUserUpdateQo.getProtocol());
        federatedFateManagerUserDoOld.setNetwork(network);

        federatedFateManagerUserDoOld.setUpdateTime(new Date());

        federatedFateManagerUserMapper.update(federatedFateManagerUserDoOld, federatedFateManagerUserDoQueryWrapper);

        return federatedFateManagerUserDoOld;
    }

    public boolean checkInstitution(InstitutionCheckQo institutionCheckQo) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("institutions", institutionCheckQo.getInstitution());

        Integer count = federatedFateManagerUserMapper.selectCount(federatedFateManagerUserDoQueryWrapper);

        return count > 0;

    }


    public boolean checkUpdateInstitution(FateManagerUserUpdateQo fateManagerUserUpdateQo) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("institutions", fateManagerUserUpdateQo.getInstitution()).ne("fate_manager_id", fateManagerUserUpdateQo.getFateManagerId());

        Integer count = federatedFateManagerUserMapper.selectCount(federatedFateManagerUserDoQueryWrapper);
        return count > 0;
    }

    public void activateFateManagerUser(HttpServletRequest httpServletRequest) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", httpServletRequest.getHeader(Dict.FATE_MANAGER_USER_ID));

        //activate fate manager user
        FederatedFateManagerUserDo federatedFateManagerUserDo = new FederatedFateManagerUserDo();
        federatedFateManagerUserDo.setStatus(2);
        federatedFateManagerUserMapper.update(federatedFateManagerUserDo, federatedFateManagerUserDoQueryWrapper);
    }

    public HashMap<String, Object> shortActivateFateManagerUser(HttpServletRequest httpServletRequest) {
        activateFateManagerUser(httpServletRequest);
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", httpServletRequest.getHeader(Dict.FATE_MANAGER_USER_ID));
        FederatedFateManagerUserDo federatedFateManagerUserDo = federatedFateManagerUserMapper.selectOne(federatedFateManagerUserDoQueryWrapper);

        HashMap<String, Object> stringObjectHashMap = new HashMap<>();
        stringObjectHashMap.put("fateManagerUser", federatedFateManagerUserDo);

        QueryWrapper<FederatedOrganizationDo> query = new QueryWrapper<>();
        query.select("id", "name", "institution", "create_time").eq("status", 1);
        FederatedOrganizationDo federatedOrganizationDo = federatedOrganizationMapper.selectOne(query);
        stringObjectHashMap.put("federatedOrganization", federatedOrganizationDo);

        return stringObjectHashMap;
    }

    public FederatedFateManagerUserDo findFateManagerUser(String fateManagerId) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", fateManagerId);
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);
        if (federatedFateManagerUserDos.size() > 0) {
            return federatedFateManagerUserDos.get(0);
        } else {
            return null;
        }
    }


    public void deleteFateManagerUser(FateManagerUserDeleteQo fateManagerUserDeleteQo) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", fateManagerUserDeleteQo.getFateManagerId());
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);

        federatedFateManagerUserMapper.delete(federatedFateManagerUserDoQueryWrapper);

        QueryWrapper<FederatedSiteManagerDo> federatedSiteManagerDoQueryWrapper = new QueryWrapper<>();
        federatedSiteManagerDoQueryWrapper.eq("institutions", federatedFateManagerUserDos.get(0).getInstitutions());

        FederatedSiteManagerDo federatedSiteManagerDo = new FederatedSiteManagerDo();
        federatedSiteManagerDo.setStatus(3);
        federatedSiteManagerMapper.update(federatedSiteManagerDo, federatedSiteManagerDoQueryWrapper);

    }

    public List<String> findAllFateManagerUserInstitutions() {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.select("institutions").eq("status", 2);
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);

        LinkedList<String> institutionsList = new LinkedList<>();
        for (FederatedFateManagerUserDo federatedFateManagerUserDo : federatedFateManagerUserDos) {
            institutionsList.add(federatedFateManagerUserDo.getInstitutions());
        }
        return institutionsList;
    }

    public PageBean<FederatedFateManagerUserDo> findPagedFateManagerUser(FateManagerUserPagedQo fateManagerUserPagedQo) {
        QueryWrapper<FederatedFateManagerUserDo> federatedCloudManagerUserDoQueryWrapper = new QueryWrapper<>();

        if (fateManagerUserPagedQo.getInstitutions() != null) {
            federatedCloudManagerUserDoQueryWrapper.like("institutions", fateManagerUserPagedQo.getInstitutions());
            fateManagerUserPagedQo.setInstitutions("%" + fateManagerUserPagedQo.getInstitutions() + "%");

        }

        federatedCloudManagerUserDoQueryWrapper.in("status", 1, 2, 3);
        Integer count = federatedFateManagerUserMapper.selectCount(federatedCloudManagerUserDoQueryWrapper);
        PageBean<FederatedFateManagerUserDo> userListBean = new PageBean<>(fateManagerUserPagedQo.getPageNum(), fateManagerUserPagedQo.getPageSize(), count);
        long startIndex = userListBean.getStartIndex();

        List<FederatedFateManagerUserDo> pagedCloudUser = federatedFateManagerUserMapper.findPagedFateManagerUser(fateManagerUserPagedQo, startIndex);

        // is it possible to reactivate
        for (FederatedFateManagerUserDo federatedFateManagerUserDo : pagedCloudUser) {
            if (federatedFateManagerUserDo.getStatus() != null && federatedFateManagerUserDo.getStatus() != 1) {
                if (federatedFateManagerUserDo.getStatus() == 3){
                    federatedFateManagerUserDo.setStatus(20);
                    continue;
                }

                QueryWrapper<FederatedSiteManagerDo> siteManagerDoQueryWrapper = new QueryWrapper<FederatedSiteManagerDo>()
                        .eq("institutions", federatedFateManagerUserDo.getInstitutions());
                Integer integer = federatedSiteManagerMapper.selectCount(siteManagerDoQueryWrapper);
                if (integer != null && integer > 0) {
                    federatedFateManagerUserDo.setStatus(20);
                }
            }
        }

        userListBean.setList(pagedCloudUser);
        return userListBean;
    }

    public boolean checkStatus(FateManagerUserUpdateQo fateManagerUserUpdateQo) {
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", fateManagerUserUpdateQo.getFateManagerId());
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);
        if (federatedFateManagerUserDos.size() <= 0) {
            return false;
        }
        FederatedFateManagerUserDo federatedFateManagerUserDo = federatedFateManagerUserDos.get(0);
        Integer status = federatedFateManagerUserDo.getStatus();
        return status == 1;

    }

    public boolean checkUrl(SiteActivateQo siteActivateQo, HttpServletRequest httpServletRequest) {

        String linkeInput = siteActivateQo.getRegistrationLink();
        if (linkeInput == null) {
            return false;
        }

        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", httpServletRequest.getHeader(Dict.FATE_MANAGER_USER_ID));
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);
        FederatedFateManagerUserDo federatedFateManagerUserDo1 = federatedFateManagerUserDos.get(0);
        if (federatedFateManagerUserDo1 == null) {
            return false;
        }
        String registrationLink = federatedFateManagerUserDo1.getRegistrationLink();
//        registrationLink = registrationLink.replaceAll("[\\s*\t\n\r]", " ");

        if (!linkeInput.equals(registrationLink)) {
            log.error("linkeInput     :{}", linkeInput);
            log.error("linkeInDateBase:{}", registrationLink);
            return false;
        }

        return true;
    }

    public List<String> findAllInstitutions() {

        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.select("institutions").in("status", 1, 2);
        List<FederatedFateManagerUserDo> federatedFateManagerUserDos = federatedFateManagerUserMapper.selectList(federatedFateManagerUserDoQueryWrapper);

        LinkedList<String> institutionsList = new LinkedList<>();
        for (FederatedFateManagerUserDo federatedFateManagerUserDo : federatedFateManagerUserDos) {
            institutionsList.add(federatedFateManagerUserDo.getInstitutions());
        }
        return institutionsList;
    }

    public boolean reactivateFateManagerUser(FateManagerUserUpdateQo fateManagerUserUpdateQo) {
        boolean result;
        QueryWrapper<FederatedFateManagerUserDo> federatedFateManagerUserDoQueryWrapper = new QueryWrapper<>();
        federatedFateManagerUserDoQueryWrapper.eq("fate_manager_id", fateManagerUserUpdateQo.getFateManagerId());
        FederatedFateManagerUserDo fateManagerUserDo = federatedFateManagerUserMapper.selectOne(federatedFateManagerUserDoQueryWrapper);

        if (result = (fateManagerUserDo != null && fateManagerUserDo.getStatus() == 2)) {
            QueryWrapper<FederatedSiteManagerDo> smw = new QueryWrapper<>();
            smw.eq("institutions", fateManagerUserDo.getInstitutions());
            List<FederatedSiteManagerDo> federatedSiteManagerDoList = federatedSiteManagerMapper.selectList(smw);

            if (result = (federatedSiteManagerDoList.isEmpty())) {
                // reset fate manager user status
                FederatedFateManagerUserDo federatedFateManagerUserDo = new FederatedFateManagerUserDo();
                federatedFateManagerUserDo.setStatus(1);
                federatedFateManagerUserDo.setUpdateTime(new Date());
                int update = federatedFateManagerUserMapper.update(federatedFateManagerUserDo, federatedFateManagerUserDoQueryWrapper);
                result = update == 1;
            }
        }
        return result;
    }
}
