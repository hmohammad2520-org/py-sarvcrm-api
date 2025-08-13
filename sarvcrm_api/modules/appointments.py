from ._base import SarvModule
from ._mixins import UrlMixin

class Appointments(SarvModule, UrlMixin):
    _module_name = 'Appointments'
    _table_name = 'appointments'
    _label_en = 'Appointments'
    _label_pr = 'بازدیدها'