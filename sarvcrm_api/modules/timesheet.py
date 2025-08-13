from ._base import SarvModule
from ._mixins import UrlMixin

class Timesheets(SarvModule, UrlMixin):
    _module_name = 'Timesheet'
    _table_name = 'timesheet'
    _label_en = 'Timesheet'
    _label_pr = 'تایم شیت'