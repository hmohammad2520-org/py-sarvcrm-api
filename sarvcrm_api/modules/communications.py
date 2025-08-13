from ._base import SarvModule
from ._mixins import UrlMixin

class Communications(SarvModule, UrlMixin):
    _module_name = 'Communications'
    _table_name = 'communications'
    _label_en = 'Communications'
    _label_pr = 'ارتباطات'