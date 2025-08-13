from ._base import SarvModule
from ._mixins import UrlMixin

class Branches(SarvModule, UrlMixin):
    _module_name = 'Branches'
    _table_name = 'branches'
    _label_en = 'Branches'
    _label_pr = 'شعب'