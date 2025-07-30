from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Campaign

class Campaigns(SarvModule, UrlMixin):
    _module_name = 'Campaigns'
    _label_en = 'Campaigns'
    _label_pr = 'کمپین ها'
    _item_class = Campaign
