from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Lead

class Leads(SarvModule, UrlMixin):
    _module_name = 'Leads'
    _label_en = 'Leads'
    _label_pr = 'سرنخ'
    _item_class = Lead
