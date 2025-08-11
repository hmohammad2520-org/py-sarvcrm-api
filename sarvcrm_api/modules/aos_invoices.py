from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosInvoice

class Invoices(SarvModule, UrlMixin):
    _module_name = 'AOS_Invoices'
    _label_en = 'Invoices'
    _label_pr = 'فاکتورها'
    _item_class = AosInvoice
