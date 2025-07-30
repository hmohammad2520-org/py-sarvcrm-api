from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Email

class Emails(SarvModule, UrlMixin):
    _module_name = 'Emails'
    _label_en = 'Emails'
    _label_pr = 'ایمیل ها'
    _item_class = Email
