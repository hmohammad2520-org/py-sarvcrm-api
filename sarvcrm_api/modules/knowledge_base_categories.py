from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import KnowledgeBaseCategory

class KnowledgeBaseCategories(SarvModule, UrlMixin):
    _module_name = 'Knowledge_Base_Categories'
    _label_en = 'Knowledge Base Categories'
    _label_pr = 'دسته پایگاه دانش'
    _item_class = KnowledgeBaseCategory
