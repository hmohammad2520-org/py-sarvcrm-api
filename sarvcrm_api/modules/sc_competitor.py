from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Competitor

class Competitors(SarvModule, UrlMixin):
    _module_name = 'sc_competitor'
    _label_en = 'Competitor'
    _label_pr = 'رقبا'
    _item_class =  Competitor