from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ServiceCenter

class ServiceCenters(SarvModule, UrlMixin):
    _module_name = 'Service_Centers'
    _label_en = 'Service Centers'
    _label_pr = 'مراکز سرویس'
    _item_class = ServiceCenter
