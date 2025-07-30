from ._base import SarvModule
from ._mixins import UrlMixin
from ..models import AsolProject

class AsolProjects(SarvModule, UrlMixin):
    _module_name = 'asol_Project'
    _label_en = 'Project'
    _label_pr = 'پروژه'
    _item_class = AsolProject
