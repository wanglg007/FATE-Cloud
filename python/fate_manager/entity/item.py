class BaseItem(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dict(self, need_none=False):
        d = {}
        for k, v in self.__dict__.items():
            if v is None and not need_none:
                continue
            d[k] = v
        return d


class IdPair(BaseItem):
    def __init__(self, **kwargs):
        self.code = None
        self.desc = None
        super(IdPair, self).__init__(**kwargs)


class AuditPair(BaseItem):
    def __init__(self, **kwargs):
        self.code = None
        self.desc = None
        self.readCode = None
        super(AuditPair, self).__init__(**kwargs)


class Role(BaseItem):
    def __init__(self, **kwargs):
        self.roleId = None
        self.roleName = None
        super(Role, self).__init__(**kwargs)


class SitePair(BaseItem):
    def __init__(self, **kwargs):
        self.partyId = None
        self.siteName = None
        self.institution = None
        super(SitePair, self).__init__(**kwargs)


class FederatedItem(BaseItem):
    def __init__(self, **kwargs):
        self.federatedId = None
        self.federatedOrganization = None
        self.institutions = None
        self.fateManagerInstitutions = None
        self.size = None
        self.siteList = []
        self.createTime = None
        super(FederatedItem, self).__init__(**kwargs)


class SiteItem(BaseItem):
    def __init__(self, **kwargs):
        self.siteId = None
        self.partyId = None
        self.siteName = None
        self.role = None
        self.status = None
        self.serviceStatus = None
        self.activationTime = None
        super(SiteItem, self).__init__(**kwargs)


class SiteVersionItem(BaseItem):
    def __init__(self, **kwargs):
        self.componentVersion = None
        self.fateServingVersion = None
        self.fateVersion = None
        super(SiteVersionItem, self).__init__(**kwargs)


class SiteSignatureItem(BaseItem):
    def __init__(self, **kwargs):
        self.partyId = None
        self.role = None
        self.appKey = None
        self.appSecret = None
        super(SiteSignatureItem, self).__init__(**kwargs)


class InstitutionSignatureItem(BaseItem):
    def __init__(self, **kwargs):
        self.fateManagerId = None
        self.appKey = None
        self.appSecret = None
        super(InstitutionSignatureItem, self).__init__(**kwargs)


class OldSignatureItem(BaseItem):
    def __init__(self, **kwargs):
        self.partyId = None
        self.role = None
        self.appKey = None
        self.appSecret = None
        super(OldSignatureItem, self).__init__(**kwargs)


class MonitorBySite(BaseItem):
    def __init__(self, **kwargs):
        self.GuestPartyId = None
        self.GuestSiteName = None
        self.GuestInstitution = None
        self.HostPartyId = None
        self.HostSiteName = None
        self.HostInstitution = None
        super(MonitorBySite, self).__init__(**kwargs)


class MonitorBase(BaseItem):
    def __init__(self, **kwargs):
        self.total = None
        self.success = None
        self.running = None
        self.waiting = None
        self.timeout = None
        self.failed = None
        self.canceled = None
        super(MonitorBase, self).__init__(**kwargs)


class JobBase(BaseItem):
    def __init__(self, **kwargs):
        self.total_jobs = None
        self.success_jobs = None
        self.success_percent = None
        self.running_jobs = None
        self.waiting_jobs = None
        self.waiting_percent = None
        self.timeout_jobs = None
        self.timeout_percent = None
        self.failed_jobs = None
        self.failed_percent = None
        super(JobBase, self).__init__(**kwargs)


class SiteMonitorByRegion(BaseItem):
    def __init__(self, **kwargs):
        self.institution_site_name = None
        self.institution = None
        self.site_name = None
        self.monitor_base = None
        super(SiteMonitorByRegion, self).__init__(**kwargs)


class MixSiteModeling(BaseItem):
    def __init__(self, **kwargs):
        self.site_name = None
        self.job_base = None
        super(MixSiteModeling, self).__init__(**kwargs)


class FateVersionItem(BaseItem):
    def __init__(self, **kwargs):
        self.id = None
        self.fate_version = None
        self.product_type = None
        self.chart_version = None
        self.version_index = None
        self.pull_status = None
        self.package_status = None
        super(FateVersionItem, self).__init__(**kwargs)

