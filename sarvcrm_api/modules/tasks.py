from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Task

class Tasks(SarvModule, UrlMixin):
    _module_name = 'Tasks'
    _table_name = 'tasks'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Tasks'
    _label_pr = 'وظایف'
    _item_class = Task
