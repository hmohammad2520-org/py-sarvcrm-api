from ._base import SarvModule
from ._mixins import UrlMixin

class AosQuotes(SarvModule, UrlMixin):
    _module_name = 'AOS_Quotes'
    _label_en = 'Quotes'
    _label_pr = 'پیش فاکتورها'