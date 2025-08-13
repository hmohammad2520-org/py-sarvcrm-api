from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Communication

class Communications(SarvModule, UrlMixin):
    _module_name = 'Communications'
    _table_name = 'communications'
    _assigned_field = ''
    _label_en = 'Communications'
    _label_pr = 'ارتباطات'
    _item_class = Communication
