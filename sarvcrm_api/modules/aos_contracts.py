from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosContract

class SalesContracts(SarvModule, UrlMixin):
    _module_name = 'AOS_Contracts'
    _table_name = 'aos_contracts'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Sales Contract'
    _label_pr = 'قراردادهای فروش'
    _item_class = AosContract
