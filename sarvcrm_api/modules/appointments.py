from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Appointment

class Appointments(SarvModule, UrlMixin):
    _module_name = 'Appointments'
    _label_en = 'Appointments'
    _label_pr = 'بازدیدها'
    _item_class = Appointment
