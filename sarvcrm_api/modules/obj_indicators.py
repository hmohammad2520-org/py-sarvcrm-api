from ._base import SarvModule
from ._mixins import UrlMixin

class ObjIndicators(SarvModule, UrlMixin):
    _module_name = 'OBJ_Indicators'
    _label_en = 'Indicators'
    _label_pr = 'شاخص'