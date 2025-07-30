from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosPdfTemplate

class AosPdfTemplates(SarvModule, UrlMixin):
    _module_name = 'AOS_PDF_Templates'
    _label_en = 'PDF Templates'
    _label_pr = 'قالب های PDF'
    _item_class = AosPdfTemplate
