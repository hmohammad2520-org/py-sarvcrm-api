from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Case

class Cases(SarvModule, UrlMixin):
    _module_name = 'Cases'
    _table_name = 'cases'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Cases'
    _label_pr = 'سرویس ها'
    _item_class = Case
