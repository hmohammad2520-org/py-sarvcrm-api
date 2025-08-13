from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Account

class Accounts(SarvModule, UrlMixin):
    _module_name = 'Accounts'
    _table_name = 'accounts'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Accounts'
    _label_pr = 'حساب ها'
    _item_class = Account
