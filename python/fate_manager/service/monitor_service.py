from fate_manager.operation.federated_db_operator import get_admin_info
from fate_manager.operation.db_operator import DBOperator
from fate_manager.entity.types import SiteStatusType
from fate_manager.entity.item import SitePair, JobBase, MonitorBase, MonitorBySite, SiteMonitorByRegion, MixSiteModeling
from fate_manager.db.db_models import FateSiteInfo, FateReportSite


def get_monitor_total(request_data):
    admin_info = get_admin_info()
    if not admin_info:
        return 100, 'no admin info found', []
    monitor_base = get_total_monitor_by_region(admin_info.get('institutions'), request_data)
    if not monitor_base:
        return 100, 'no monitor base details data found', []
    monitor_by_site_list = get_site_monitor_by_region(request_data)
    if not monitor_by_site_list:
        return 100, 'no monitor site list data found', []
    for monitor_by_site in monitor_by_site_list:
        site_info = {
            'PartyId': monitor_by_site.get('GuestPartyId'),
            'Status': SiteStatusType.JOINED
        }
        site_list = DBOperator.query_entity(FateSiteInfo,
                                            party_id=site_info.get('PartyId'), status=site_info.get('Status'))
        item_base = monitor_by_site.get('MonitorBase').copy()
        item_base['Failed'] = item_base.get('Timeout', 0) + item_base.get('Canceled', 0)
        if len(site_list) > 0:
            site_pair = SitePair(partyId=monitor_by_site.get('GuestPartyId'),
                                 siteName=monitor_by_site.get('GuestSiteName'),
                                 institution=monitor_by_site.get('GuestInstitution'))
    # TODO to be completed


    return 0, 'success', []


def get_total_monitor_by_region(institution: str, request_data):
    sql = f"SELECT COUNT(DISTINCT if(host_institution={institution},host_party_id, guest_party_id)) active_data, " \
          "COUNT(job_id) total, SUM(if(status='success',1,0)) success, SUM(if(status='running',1,0)) running, " \
          "SUM(if(status='waiting',1,0)) waiting, SUM(if(status='timeout',1,0)) timeout, " \
          "SUM(if(status='canceled',1,0)) canceled, SUM(if(status='failed',1,0)) failed FROM t_fate_monitor_detail " \
          f"WHERE ds >= {request_data.get('startDate')} AND ds <= {request_data.get('endDate')} AND guest_site_name != ''"
    result = DBOperator.query_with_raw_sql(sql=sql)
    query_set = next(result)
    if query_set:
        res = dict(zip(['ActiveData', 'Total', 'Success', 'Running',
                        'Waiting', 'Timeout', 'Canceled', 'Failed'],
                       list(query_set)))
        monitor_base = MonitorBase(**res)
        data = {
            'MonitorBase': monitor_base.to_dict(),
            'ActiveData': res.get('ActiveData')
        }
    else:
        data = {}
    return data


def get_site_monitor_by_region(institution: str, request_data):
    sql = "SELECT guest_party_id, guest_site_name, guest_institution, host_institution, host_party_id, " \
          "host_site_name, COUNT(job_id) total, SUM(if(status='success',1,0)) success, " \
          "SUM(if(status='running',1,0)) running, SUM(if(status='waiting',1,0)) waiting, " \
          "SUM(if(status='timeout',1,0)) timeout, SUM(if(status='canceled',1,0)) canceled, " \
          "SUM(if(status='failed',1,0)) failed FROM t_fate_monitor_detail " \
          f"WHERE ds >= {request_data.get('startDate')} AND ds <= {request_data.get('endDate')} AND guest_site_name != '' " \
          "GROUP BY guest_party_id,host_party_id"
    result = DBOperator.query_with_raw_sql(sql=sql)
    data = []
    for query_set in result:
        query_data = dict(zip(['GuestPartyId', 'GuestSiteName', 'GuestInstitution', 'HostInstitution',
                                      'HostPartyId', 'HostSiteName', 'Total', 'Success', 'Running',
                                      'Waiting', 'Timeout', 'Canceled', 'Failed'],
                                 list(query_set)))
        monitor_base =  MonitorBase(**query_data)
        monitor_by_site = MonitorBySite(**query_data).to_dict()
        monitor_by_site['MonitorBase'] = monitor_base
        data.append(monitor_by_site)
    return data


def get_report_institution_region(request_data):
    sql = "SELECT institution, SUM(total) total, SUM(success) success, SUM(running) running, " \
          "SUM(timeout) timeout, SUM(canceled) canceled, SUM(failed) failed " \
          "FROM t_fate_report_institution" \
          f"WHERE ds >= {request_data.get('startDate')} AND ds <= {request_data.get('endDate')} " \
          f"GROUP BY institution"
    return DBOperator.query_with_raw_sql(sql)


def get_institution_base_statics(request_data):
    account_info = get_admin_info()
    institution = account_info.institutions
    monitor_base = get_total_monitor_by_region(institution, request_data)

    monitor_by_institution_list = get_report_institution_region(request_data)

    data = []

    if monitor_by_institution_list:
        for institution_site in monitor_by_institution_list:
            data.append(
                {
                    "institution": institution_site.institution,
                    "jobbase": JobBase(totalJobs=institution_site.total, successJobs=institution_site.success,
                                       runningJobs=institution_site.running, waitingJobs=institution_site.waiting,
                                       timeoutJobs=institution_site.timeout, failedJobs=institution_site.failed,
                                       successPercent=round(institution_site.success / institution_site.total, 4),
                                       runningPercent=round(institution_site.running / institution_site.total, 4),
                                       waitingPercent=round(institution_site.waiting/institution_site.total, 4),
                                       timeoutPercent=round(institution_site.timeout/institution_site.total, 4)).to_dict()
                }
            )

        monitor_base_info = monitor_base.get('MonitorBase', {})
        resp = {
            "jobbase": JobBase(totalJobs=monitor_base_info.total, successJobs=monitor_base_info.success,
                               runningJobs=monitor_base_info.running, waitingJobs=monitor_base_info.waiting,
                               timeoutJobs=monitor_base_info.timeout, failedJobs=monitor_base_info.failed,
                               successPercent=round(monitor_base_info.success / monitor_base_info.total, 4),
                               runningPercent=round(monitor_base_info.running / monitor_base_info.total, 4),
                               waitingPercent=round(monitor_base_info.waiting/monitor_base_info.total, 4),
                               timeoutPercent=round(monitor_base_info.timeout/monitor_base_info.total, 4)).to_dict(),
            "data": data,
            "total": len(data)
        }
        return 0, 'success', resp
    return 100, 'failed', {}


def get_institution_site_list(request_data):
    sql = "SELECT institution_site_name FROM t_fate_report_site " \
          f"WHERE ds >= {request_data.get('startDate')} AND ds <= {request_data.get('endDate')}" \
          "GROUP BY institution_site_name ORDER create_time"

    query_res = DBOperator.query_with_raw_sql(sql)
    return [site.institution_site_name for site in query_res] if query_res else []


def get_report_site_region(request_data, institution_list):
    sql = "SELECT institution, institution_site_name, site_name, " \
          "SUM(total) total, SUM(success) success, SUM(running) running, SUM(waiting) waiting, " \
          "SUM(timeout) timeout, SUM(canceled) canceled, SUM(failed) failed " \
          "FROM t_fate_report_site" \
          f"WHERE ds >= {request_data.get('startDate')} AND ds <= {request_data.get('endDate')} " \
          f"AND institution_site_name in {institution_list}" \
          "GROUP BY institution, institution_site_name, site_name " \
          f"LIMIT {request_data.get('PageSize', 15)} " \
          f"OFFSET {request_data.get('PageNum', 1) * request_data.get('PageSize', 15)}"

    query_res = DBOperator.query_with_raw_sql(sql)
    data = []
    for site in query_res:
        monitor_base_info = MonitorBase(total=site.total, success=site.success, running=site.running,
                                        waiting=site.waiting, timeout=site.timeout, canceled=site.canceled,
                                        failed=site.failed).to_dict()
        site_monitor_by_region_info = SiteMonitorByRegion(institution_site_name=site.institution_site_name,
                                                          institution=site.institution, site_name=site.site_name,
                                                          monitor_base=monitor_base_info).to_dict()
        data.append(site_monitor_by_region_info)
    return data


def get_site_base_statics(request_data):
    if request_data.get('PageSize', 0) == 0 and request_data.get('PageNum', 0) == 0:
        request_data['PageSize'] = 15
        request_data['PageNum'] = 1

    institution_site_name_list = get_institution_site_list(request_data)

    site_monitor_by_region_list = get_report_site_region(request_data, institution_site_name_list)

    data = {}
    row_list = []

    for item in site_monitor_by_region_list:
        institution = item.institution
        institution_site_name = item.institution_site_name
        site_name = item.site_name
        monitor_base = item.monitor_base

        hit_tag = False
        if site_name in row_list:
            hit_tag = True
        if not hit_tag:
            row_list.append(site_name)

        monitor_base['failed'] = monitor_base.get('failed') + monitor_base.get('timeout') + monitor_base.get('canceled')

        site_monitor = {
            'site_name': site_name,
            'monitor_base': monitor_base
        }

        if institution in data:
            site_monitor_map = data[institution]
            if institution_site_name not in site_monitor_map:
                site_monitor_map[institution_site_name] = []
            site_monitor_map[institution_site_name].append(site_monitor)
        else:
            site_monitor_map = {}
            site_monitor_map[institution_site_name] = [site_monitor]
            data[institution] = site_monitor_map

    other_site_list = []
    for key, value in data.items():
        institution = key
        institution_site_list = []
        for institution_site_name, site_monitor_list in value.items():
            mix_site_modeling_list = []
            for site_monitor in site_monitor_list:
                job_base = JobBase(total_jobs=site_monitor.get('total'), success_jobs=site_monitor.get('success'),
                                   running_jobs=site_monitor.get('running'), waiting_jobs=site_monitor.get('waiting'),
                                   timeout_jobs=site_monitor.get('timeout'),
                                   failed_jobs=site_monitor.get('timeout')+site_monitor.get('failed')+site_monitor.get('canceled'),
                                   success_percent=site_monitor.get('success')/site_monitor.get('total'),
                                   running_percent=site_monitor.get('running')/site_monitor.get('total'),
                                   waiting_percent=site_monitor.get('waiting')/site_monitor.get('total'),
                                   timeout_percent=site_monitor.get('timeout')/site_monitor.get('total')).to_dict()
                mix_site_modeling = MixSiteModeling(site_name=site_monitor.get('site_name'),
                                                    job_base=job_base)
                mix_site_modeling_list.append(mix_site_modeling)

            if len(site_monitor_list) < len(row_list):
                for site_name in row_list:
                    hit_tag = False
                    for site_monitor in site_monitor_list:
                        if site_monitor.get('site_name') == site_name:
                            hit_tag = True
                            break
                    if not hit_tag:
                        job_base = JobBase(total_jobs=0, success_jobs=0, running_jobs=0,  waiting_jobs=0,
                                           timeout_jobs=0, failed_jobs=0, success_percent=0.00,  running_percent=0.00,
                                           waiting_percent=0.00, failed_percent=0.00).to_dict()
                        mix_site_modeling = MixSiteModeling(site_name=site_name, job_base=job_base)
                        mix_site_modeling_list.append(mix_site_modeling)


            institution_site_list.append({
                'institutionSiteName': institution_site_name,
                'mixSiteModeling': mix_site_modeling_list
            })

        other_site_list.append({
            'institution': institution,
            'institutionSiteList': institution_site_list
        })

    if row_list:
        resp = {
            'siteList': row_list,
            'data': other_site_list,
            'total': len(institution_site_name_list)
        }
        return 0, 'success', resp
    return 100, 'failed', {}












