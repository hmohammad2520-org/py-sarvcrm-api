from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Case

class Cases(SarvModule, UrlMixin):
    _module_name = 'Cases'
    _label_en = 'Cases'
    _label_pr = 'سرویس ها'
    _item_class = Case
