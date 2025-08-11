from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Sheet

class Timesheets(SarvModule, UrlMixin):
    _module_name = 'Timesheet'
    _label_en = 'Timesheet'
    _label_pr = 'تایم شیت'
    _item_class = Sheet
