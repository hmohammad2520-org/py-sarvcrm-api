from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Document

class Documents(SarvModule, UrlMixin):
    _module_name = 'Documents'
    _label_en = 'Documents'
    _label_pr = 'اسناد'
    _item_class = Document
