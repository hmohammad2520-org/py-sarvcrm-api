from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Approval

class Approvals(SarvModule, UrlMixin):
    _module_name = 'Approval'
    _label_en = 'Approval'
    _label_pr = 'تاییدیه'
    _item_class = Approval
