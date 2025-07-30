from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import User

class Users(SarvModule, UrlMixin):
    _module_name = 'Users'
    _label_en = 'Users'
    _label_pr = 'کاربران'
    _item_class = User
