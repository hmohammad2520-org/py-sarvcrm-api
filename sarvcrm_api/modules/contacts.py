from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Contact

class Contacts(SarvModule, UrlMixin):
    _module_name = 'Contacts'
    _label_en = 'Contacts'
    _label_pr = 'افراد'
    _item_class = Contact
