from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Meeting

class Meetings(SarvModule, UrlMixin):
    _module_name = 'Meetings'
    _label_en = 'Meetings'
    _label_pr = 'جلسات'
    _item_class = Meeting
