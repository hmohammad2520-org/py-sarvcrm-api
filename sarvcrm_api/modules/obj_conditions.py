from ._base import SarvModule
from ._mixins import UrlMixin

class ObjConditions(SarvModule, UrlMixin):
    _module_name = 'OBJ_Conditions'
    _label_en = 'Conditions'
    _label_pr = 'شرایط شاخص'