from ._base import SarvModule
from ._mixins import UrlMixin

class Tasks(SarvModule, UrlMixin):
    _module_name = 'Tasks'
    _table_name = 'tasks'
    _label_en = 'Tasks'
    _label_pr = 'وظایف'