from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ObjObjective

class Objectives(SarvModule, UrlMixin):
    _module_name = 'OBJ_Objectives'
    _table_name = 'obj_objectives'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Objectives'
    _label_pr = 'اهداف'
    _item_class = ObjObjective
