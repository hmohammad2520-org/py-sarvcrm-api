from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Opportunity

class Opportunities(SarvModule, UrlMixin):
    _module_name = 'Opportunities'
    _label_en = 'Opportunities'
    _label_pr = 'فرصت ها'
    _item_class = Opportunity
