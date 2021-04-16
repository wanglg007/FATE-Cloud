class UserRole:
    UNKNOWN = -1
    ADMIN = 1
    DEVELOPER = 2
    BUSINESS = 3

    @staticmethod
    def to_str(role: int):
        if role == UserRole.UNKNOWN:
            return "unknown"
        elif role == UserRole.ADMIN:
            return "Admin"
        elif role == UserRole.DEVELOPER:
            return "Developer or OP"
        elif role == UserRole.BUSINESS:
            return "Business or Data Analyst"


class RoleType:
    UNKNOWN = -1
    GUEST = 1
    HOST = 2
    ARBITER = 3

    @staticmethod
    def to_str(role: int):
        if role == RoleType.UNKNOWN:
            return "unknown"
        elif role == RoleType.GUEST:
            return "Guest"
        elif role == RoleType.HOST:
            return "Host"
        elif role == RoleType.ARBITER:
            return "Arbiter"


class PermissionType:
    UNKNOWN = -1
    BASIC = 1
    DEPLOY = 2
    FATEBOARD = 3
    FATESTUDIO = 4

    @staticmethod
    def to_str(role: int):
        if role == PermissionType.UNKNOWN:
            return "unknown"
        elif role == PermissionType.BASIC:
            return "FATE Cloud: Basic management"
        elif role == PermissionType.DEPLOY:
            return "FATE Cloud: Auto-deploy"
        elif role == PermissionType.FATEBOARD:
            return "FATE-Board"
        elif role == PermissionType.FATESTUDIO:
            return "FATE-Studio"


class ActivateStatus:
    NO = 0
    YES = 1
    DELETE = 2


class IsValidType:
    UNKNOWN = -1
    NO = 0
    YES = 1
    ING = 2

    @staticmethod
    def to_str(status: int):
        if status == IsValidType.UNKNOWN:
            return "unknown"
        elif status == IsValidType.YES:
            return "valid"
        elif status == IsValidType.NO:
            return "unvalid"
        elif status == IsValidType.ING:
            return "wait for valid"


class SiteStatusType:
    UNKNOWN = -1
    NO_JOIN = 1
    JOINED = 2
    REMOVED = 3

    @staticmethod
    def to_str(role: int):
        if role == SiteStatusType.UNKNOWN:
            return "unknown"
        elif role == SiteStatusType.NO_JOIN:
            return "Not Join"
        elif role == SiteStatusType.JOINED:
            return "Joined"
        elif role == SiteStatusType.REMOVED:
            return "Deleted"


class SiteRunStatusType:
    UNKNOWN = -1
    STOPPED = 1
    RUNNING = 2

    @staticmethod
    def to_str(status: int):
        if status == SiteRunStatusType.UNKNOWN:
            return "unknown"
        elif status == SiteRunStatusType.STOPPED:
            return "stopped"
        elif status == SiteRunStatusType.RUNNING:
            return "running"


class AuditStatusType:
    UNKNOWN = -1
    AUDITING = 1
    AGREED = 2
    REJECTED = 3
    CANCEL = 4

    @staticmethod
    def to_str(status):
        if status == AuditStatusType.UNKNOWN:
            return "unknown"
        elif status == AuditStatusType.AUDITING:
            return "Waiting For Cloud Audit!"
        elif status == AuditStatusType.AGREED:
            return "Agreed Apply"
        elif status == AuditStatusType.REJECTED:
            return "Rejected Apply"
        elif status == AuditStatusType.CANCEL:
            return "Cancel Apply"


class ApplyReadStatusType:
    UNKNOWN = -1
    NOT_READ = 0
    READ = 1

    @staticmethod
    def to_str(status):
        if status == ApplyReadStatusType.NOT_READ:
            return "Apply Site No Read"
        elif status == ApplyReadStatusType.READ:
            return "Apply Site Read"
        else:
            return "unknown"


class ReadStatusType:
    UNKNOWN = -1
    AGREED = 1
    REJECTED = 2
    READ = 3

    @staticmethod
    def to_str(status):
        if status == ReadStatusType.AGREED:
            return "Successfully changed the Network configuration!"
        elif status == ReadStatusType.REJECTED:
            return "Changed the Network configuration failed!"
        elif status == ReadStatusType.READ:
            return "Read"
        else:
            return "unknown"


class EditType:
    UNKNOWN = -1
    NO = 1
    YES = 2

    @staticmethod
    def to_str(status):
        if status == EditType.NO:
            return "unedit"
        elif status == EditType.YES:
            return "edit"
        else:
            return "unknown"


class ServiceStatusType:
    UNKNOWN = -1
    UNAVAILABLE = 1
    AVAILABLE = 2

    @staticmethod
    def to_str(status: int):
        if status == ServiceStatusType.UNKNOWN:
            return "unknown"
        elif status == ServiceStatusType.AVAILABLE:
            return "Available"
        elif status == ServiceStatusType.UNAVAILABLE:
            return "Unavaiable"


class LogDealType:
    UNKNOWN = -1
    NO = 0
    AGREED = 1
    REJECTED = 2

    @staticmethod
    def to_str(status: int):
        if status == LogDealType.UNKNOWN:
            return "unknown"
        elif status == LogDealType.NO:
            return "not deal"
        elif status == LogDealType.AGREED:
            return "agreed"
        elif status == LogDealType.REJECTED:
            return "rejected"



class FuncDebug:
    UNKNOWN = -1
    ON = 1
    OFF = 2


class DeployType:
    UNKNOWN = -1
    KUBEFATE = 1
    HYPERION = 2


class PackageStatus:
    UNKNOWN = -1
    NO = 0
    YES = 1
    FAILED = 2
    PULLING = 3

    @classmethod
    def to_str(cls, status: int):
        if status == cls.PULLING:
            return "pulling"
        elif status == cls.NO:
            return "no"
        elif status == cls.YES:
            return "yes"
        elif status == cls.FAILED:
            return "failed"
        else:
            return "unknown"


class DeployStatus:
    UNKNOWN = -1
    SUCCESS = 0
    LOADING = 1
    LOADED = 2
    LOAD_FAILED = 3
    UNDER_INSTALLATION = 4
    INSTALLING = 5
    INSTALLED = 6
    INSTALLED_FAILED = 7
    IN_TESTING = 8
    TEST_PASSED = 9
    TEST_FAILED = 10

    def to_str(self, status):
        if status == DeployStatus.SUCCESS:
            return 'success'
        elif status == DeployStatus.LOADING:
            return 'loading'
        elif status == DeployStatus.LOADED:
            return 'loaded'
        elif status == DeployStatus.LOAD_FAILED:
            return 'load_failed'
        elif status == DeployStatus.UNDER_INSTALLATION:
            return 'under_installation'
        elif status == DeployStatus.INSTALLING:
            return 'installing'
        elif status == DeployStatus.INSTALLED:
            return 'installed'
        elif status == DeployStatus.INSTALLED_FAILED:
            return 'installed_falied'
        elif status == DeployStatus.IN_TESTING:
            return 'in_testing'
        elif status == DeployStatus.TEST_PASSED:
            return 'test_passed'
        elif status == DeployStatus.TEST_FAILED:
            return 'test_failed'
        return 'unknown'




class ProductType:
    UNKNOWN = -1
    FATE = 1
    FATE_SERVING = 2

    @staticmethod
    def to_str(status: int):
        if status == ProductType.UNKNOWN:
            return "unknown"
        elif status == ProductType.FATE:
            return "FATE"
        elif status == ProductType.FATE_SERVING:
            return "Serving"


class ToyTestOnlyType:
    UNKNOWN = -1
    NO_TEST = 0
    TESTING = 1
    SUCCESS = 2
    FAILED = 3

    @staticmethod
    def to_str(status: int):
        if status == ToyTestOnlyType.UNKNOWN:
            return "unknown"
        elif status == ToyTestOnlyType.NO_TEST:
            return "no test"
        elif status == ToyTestOnlyType.TESTING:
            return "in testing"
        elif status == ToyTestOnlyType.SUCCESS:
            return "test success"
        elif status == ToyTestOnlyType.FAILED:
            return "toy test failed"


class IsValid:
    UNKNOWN = -1
    NO = 0
    YES = 1
    ING = 2


class ClickType:
    UNKNOWN = -1
    CONNECT = 1
    PREPARE = 2
    SYSTEM_CHECK = 3
    ANSIBLE_INSTALL = 4
    ACQUISITION = 5
    INSTALL = 6
    TEST = 7


class TestStatus:
    UNKNOWN = -1
    WAITING = 0
    TESTING = 1
    YES = 2
    NO = 3

    @staticmethod
    def to_str(status: int):
        if status == TestStatus.WAITING:
            return 'waiting'
        elif status == TestStatus.TESTING:
            return 'testing'
        elif status == TestStatus.YES:
            return 'yes'
        elif status == TestStatus.NO:
            return 'no'
        else:
            return 'unknown'


class TestItem:
    UNKNWON = -1
    POD = 0
    SINGLE = 1
    TOY = 2
    FAST = 3
    NORMAL = 4

    @staticmethod
    def to_str(status: int):
        if status == TestItem.POD:
            return 'Pod/SVC Status Of Each Component'
        elif status == TestItem.SINGLE:
            return 'Single Test'
        elif status == TestItem.TOY:
            return 'Toy test'
        elif status == TestItem.FAST:
            return 'Minimize Fast Test'
        elif status == TestItem.NORMAL:
            return 'Minimize Normal Test'
        else:
            return 'default'


class ToyTestOnlyTypeRead:
    UNKNOWN = -1
    YES = 0
    NO = 1


class SiteRunStatus:
    UNKNOWN = -1
    STOPPED = 1
    RUNNING = 2


class ToyTestOnly:
    UNKNOWN = -1
    NO_TEST = 0
    TESTING = 1
    SUCCESS = 2
    FAILED = 3


class ToyTestOnlyRead:
    UNKNOWN = -1
    YES = 0
    NO = 1


class SiteStatus:
    UNKNOWN = -1
    NO_JOIN = 1
    JOINED = 2
    REMOVED = 3


class JobType:
    UNKNOWN = -1
    INSTALL = 0
    UPDATE = 1
    DELETE = 2


class JobStatus:
    UNKNOWN = -1
    SUCCESS = 0
    RUNNING = 1
    FAILED = 2


class ServiceStatus:
    UNKNOWN = -1
    UNAVAILABLE = 1
    AVAILABLE = 2