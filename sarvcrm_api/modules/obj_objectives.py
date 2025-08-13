from ._base import SarvModule
from ._mixins import UrlMixin

class Objectives(SarvModule, UrlMixin):
    _module_name = 'OBJ_Objectives'
    _table_name = 'obj_objectives'
    _label_en = 'Objectives'
    _label_pr = 'اهداف'