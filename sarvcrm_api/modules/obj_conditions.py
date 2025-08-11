from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ObjCondition

class Conditions(SarvModule, UrlMixin):
    _module_name = 'OBJ_Conditions'
    _label_en = 'Conditions'
    _label_pr = 'شرایط شاخص'
    _item_class = ObjCondition
