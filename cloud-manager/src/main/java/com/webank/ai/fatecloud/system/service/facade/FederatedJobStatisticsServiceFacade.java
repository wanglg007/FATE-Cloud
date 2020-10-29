package com.webank.ai.fatecloud.system.service.facade;

import com.webank.ai.fatecloud.common.CheckSignature;
import com.webank.ai.fatecloud.common.CommonResponse;
import com.webank.ai.fatecloud.common.Enum.ReturnCodeEnum;
import com.webank.ai.fatecloud.system.pojo.dto.*;
import com.webank.ai.fatecloud.system.pojo.qo.*;
import com.webank.ai.fatecloud.system.service.impl.FederatedJobStatisticsService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
public class FederatedJobStatisticsServiceFacade {

    @Autowired
    FederatedJobStatisticsService federatedJobStatisticsService;

    @Autowired
    CheckSignature checkSignature;

    public CommonResponse pushJosStatistics(List<JobStatisticsQo> jobStatisticsQos) {
        //check authority
        //todo
//        boolean result = checkSignature.checkSignatureNew(httpServletRequest, JSON.toJSONString(authorityInstitutionsQo), Dict.FATE_MANAGER_USER, new int[]{2}, null);
//        if (!result) {
//            return new CommonResponse(ReturnCodeEnum.AUTHORITY_ERROR);
//        }
        if (!(jobStatisticsQos.size() > 0)) {
            return new CommonResponse<>(ReturnCodeEnum.PARAMETERS_ERROR);
        }
        federatedJobStatisticsService.pushJosStatistics(jobStatisticsQos);
        return new CommonResponse<>(ReturnCodeEnum.SUCCESS);

    }

    public CommonResponse<JobStatisticsOfSiteDimensionDto> getJobStatisticsOfSiteDimension(JobOfSiteDimensionQo jobOfSiteDimensionQo) {
        JobStatisticsOfSiteDimensionDto jobStatisticsOfSiteDimensionDto = federatedJobStatisticsService.getJobStatisticsOfSiteDimension(jobOfSiteDimensionQo);
        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsOfSiteDimensionDto);
    }

    public CommonResponse<List<JobStatisticOfInstitutionsDimensionDto>> getJobStatisticsODimension(JobOfSiteDimensionQo jobOfSiteDimensionQo) {
        List<JobStatisticOfInstitutionsDimensionDto> jobStatisticsODimensionList = federatedJobStatisticsService.getJobStatisticsODimension(jobOfSiteDimensionQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsODimensionList);

    }

    public CommonResponse<JobStatisticsSummaryTodayInstitutionsAllDto> getJobStatisticsSummaryTodayInstitutionsAll(JobStatisticsSummaryTodayQo jobStatisticsSummaryTodayQo) {
        JobStatisticsSummaryTodayInstitutionsAllDto jobStatisticsSummary = federatedJobStatisticsService.getJobStatisticsSummaryTodayInstitutionsAll(jobStatisticsSummaryTodayQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummary);
    }

    public CommonResponse<List<JobStatisticsSummaryTodayInstitutionsEachDto>> getJobStatisticsSummaryTodayInstitutionsEach(JobStatisticsSummaryTodayQo jobStatisticsSummaryTodayQo) {
        List<JobStatisticsSummaryTodayInstitutionsEachDto> jobStatisticsSummaryTodayInstitutionsEachDtos = federatedJobStatisticsService.getJobStatisticsSummaryTodayInstitutionsEach(jobStatisticsSummaryTodayQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodayInstitutionsEachDtos);

    }

    public CommonResponse<JobStatisticsSummaryTodaySiteAllDto> getJobStatisticsSummaryTodaySiteAll(JobStatisticsSummaryTodaySiteAllQo jobStatisticsSummaryTodaySiteAllQo) {
        JobStatisticsSummaryTodaySiteAllDto jobStatisticsSummaryTodaySiteAllDto = federatedJobStatisticsService.getJobStatisticsSummaryTodaySiteAll(jobStatisticsSummaryTodaySiteAllQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodaySiteAllDto);
    }

    public CommonResponse<List<JobStatisticsSummaryTodaySiteEachDto>> getJobStatisticsSummaryTodaySiteEach(JobStatisticsSummaryTodaySiteAllQo jobStatisticsSummaryTodaySiteAllQo) {

        List<JobStatisticsSummaryTodaySiteEachDto> jobStatisticsSummaryTodaySiteEachDtos=federatedJobStatisticsService.getJobStatisticsSummaryTodaySiteEach(jobStatisticsSummaryTodaySiteAllQo);
        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodaySiteEachDtos);
    }

    public CommonResponse<JobStatisticsOfSiteDimensionDto> getJobStatisticsOfSiteDimensionForPeriod(JobOfSiteDimensionPeriodQo jobOfSiteDimensionPeriodQo) {
        JobStatisticsOfSiteDimensionDto jobStatisticsOfSiteDimensionDto = federatedJobStatisticsService.getJobStatisticsOfSiteDimensionForPeriod(jobOfSiteDimensionPeriodQo);
        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsOfSiteDimensionDto);
    }

    public CommonResponse<List<JobStatisticOfInstitutionsDimensionDto>> getJobStatisticsODimensionForPeriod(JobOfSiteDimensionPeriodQo jobOfSiteDimensionPeriodQo) {
        List<JobStatisticOfInstitutionsDimensionDto> jobStatisticsODimensionList = federatedJobStatisticsService.getJobStatisticsODimensionForPeriod(jobOfSiteDimensionPeriodQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsODimensionList);    }

    public CommonResponse<JobStatisticsSummaryTodayInstitutionsAllDto> getJobStatisticsSummaryInstitutionsAllForPeriod(JobStatisticsSummaryForPeriodQo jobStatisticsSummaryForPeriodQo) {
        JobStatisticsSummaryTodayInstitutionsAllDto jobStatisticsSummary = federatedJobStatisticsService.getJobStatisticsSummaryInstitutionsAllForPeriod(jobStatisticsSummaryForPeriodQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummary);

    }

    public CommonResponse<List<JobStatisticsSummaryTodayInstitutionsEachDto>> getJobStatisticsSummaryInstitutionsEachForPeriod(JobStatisticsSummaryForPeriodQo jobStatisticsSummaryForPeriodQo) {
        List<JobStatisticsSummaryTodayInstitutionsEachDto> jobStatisticsSummaryTodayInstitutionsEachDtos = federatedJobStatisticsService.getJobStatisticsSummaryInstitutionsEachForPeriod(jobStatisticsSummaryForPeriodQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodayInstitutionsEachDtos);

    }

    public CommonResponse<JobStatisticsSummaryTodaySiteAllDto> getJobStatisticsSummarySiteAllForPeriod(JobStatisticsSummarySiteAllForPeriodQo jobStatisticsSummarySiteAllForPeriodQo) {
        JobStatisticsSummaryTodaySiteAllDto jobStatisticsSummaryTodaySiteAllDto = federatedJobStatisticsService.getJobStatisticsSummarySiteAllForPeriod(jobStatisticsSummarySiteAllForPeriodQo);

        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodaySiteAllDto);

    }

    public CommonResponse<List<JobStatisticsSummaryTodaySiteEachDto>> getJobStatisticsSummarySiteEachForPeriod(JobStatisticsSummarySiteAllForPeriodQo jobStatisticsSummarySiteAllForPeriodQo) {
        List<JobStatisticsSummaryTodaySiteEachDto> jobStatisticsSummaryTodaySiteEachDtos=federatedJobStatisticsService.getJobStatisticsSummarySiteEachForPeriod(jobStatisticsSummarySiteAllForPeriodQo);
        return new CommonResponse<>(ReturnCodeEnum.SUCCESS, jobStatisticsSummaryTodaySiteEachDtos);
    }
}
