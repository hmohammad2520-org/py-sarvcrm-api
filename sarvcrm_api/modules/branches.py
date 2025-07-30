from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Branch

class Branches(SarvModule, UrlMixin):
    _module_name = 'Branches'
    _label_en = 'Branches'
    _label_pr = 'شعب'
    _item_class = Branch
