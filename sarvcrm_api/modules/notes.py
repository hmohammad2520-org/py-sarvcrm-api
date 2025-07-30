from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Note

class Notes(SarvModule, UrlMixin):
    _module_name = 'Notes'
    _label_en = 'Notes'
    _label_pr = 'یادداشت ها'
    _item_class = Note
