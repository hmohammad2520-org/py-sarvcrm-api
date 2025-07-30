from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import Deposit

class Deposits(SarvModule, UrlMixin):
    _module_name = 'Deposits'
    _label_en = 'Deposits'
    _label_pr = 'ودیعه'
    _item_class = Deposit
