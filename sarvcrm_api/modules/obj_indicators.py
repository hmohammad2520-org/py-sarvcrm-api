from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ObjIndicator

class ObjIndicators(SarvModule, UrlMixin):
    _module_name = 'OBJ_Indicators'
    _label_en = 'Indicators'
    _label_pr = 'شاخص'
    _item_class = ObjIndicator
