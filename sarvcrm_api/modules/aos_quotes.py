from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosQuote

class Quotes(SarvModule, UrlMixin):
    _module_name = 'AOS_Quotes'
    _label_en = 'Quotes'
    _label_pr = 'پیش فاکتورها'
    _item_class = AosQuote
