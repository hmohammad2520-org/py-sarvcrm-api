from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AosPdfTemplate

class PDFTemplates(SarvModule, UrlMixin):
    _module_name = 'AOS_PDF_Templates'
    _table_name = 'aos_pdf_templates'
    _assigned_field = 'assigned_user_id'
    _label_en = 'PDF Templates'
    _label_pr = 'قالب های PDF'
    _item_class = AosPdfTemplate
