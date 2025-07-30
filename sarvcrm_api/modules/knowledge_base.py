from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import KnowledgeBase

class KnowledgeBases(SarvModule, UrlMixin):
    _module_name = 'Knowledge_Base'
    _label_en = 'Knowledge Base'
    _label_pr = 'پایگاه دانش'
    _item_class = KnowledgeBase
