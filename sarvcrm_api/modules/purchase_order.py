from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import PurchaseOrder

class PurchaseOrders(SarvModule, UrlMixin):
    _module_name = 'Purchase_Order'
    _label_en = 'Purchase Order'
    _label_pr = 'سفارش خرید'
    _item_class = PurchaseOrder