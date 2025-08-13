from ._base import SarvModule
from ._mixins import UrlMixin

class Meetings(SarvModule, UrlMixin):
    _module_name = 'Meetings'
    _table_name = 'meetings'
    _label_en = 'Meetings'
    _label_pr = 'جلسات'