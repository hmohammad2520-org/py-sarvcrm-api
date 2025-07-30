from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Service

class Services(SarvModule, UrlMixin):
    _module_name = 'sc_contract_management'
    _label_en = 'Services'
    _label_pr = 'خدمات'
    _item_class = Service