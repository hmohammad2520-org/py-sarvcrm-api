from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosProduct

class Products(SarvModule, UrlMixin):
    _module_name = 'AOS_Products'
    _label_en = 'Products'
    _label_pr = 'محصولات'
    _item_class = AosProduct
