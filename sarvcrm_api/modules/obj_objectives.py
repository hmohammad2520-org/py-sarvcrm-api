from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ObjObjective

class ObjObjectives(SarvModule, UrlMixin):
    _module_name = 'OBJ_Objectives'
    _label_en = 'Objectives'
    _label_pr = 'اهداف'
    _item_class = ObjObjective
