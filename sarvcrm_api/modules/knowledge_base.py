from ._base import SarvModule
from ._mixins import UrlMixin

class KnowledgeBases(SarvModule, UrlMixin):
    _module_name = 'Knowledge_Base'
    _table_name = 'knowledge_base'
    _label_en = 'Knowledge Base'
    _label_pr = 'پایگاه دانش'