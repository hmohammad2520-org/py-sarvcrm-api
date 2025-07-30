from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import CommunicationsTarget

class CommunicationsTargets(SarvModule, UrlMixin):
    _module_name = 'Communications_Target'
    _label_en = 'Communications Target'
    _label_pr = 'هدف ارتباطات'
    _item_class = CommunicationsTarget
