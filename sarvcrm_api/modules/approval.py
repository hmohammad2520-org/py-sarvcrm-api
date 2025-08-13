from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Approval

class Approvals(SarvModule, UrlMixin):
    _module_name = 'Approval'
    _table_name = 'approval'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Approval'
    _label_pr = 'تاییدیه'
    _item_class = Approval
