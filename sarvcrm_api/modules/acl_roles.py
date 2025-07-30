from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import ACLRole

class ACLRoles(SarvModule, UrlMixin):
    _module_name = 'ACLRoles'
    _label_en = 'ACL Roles'
    _label_pr = 'نقش ها'
    _item_class = ACLRole
