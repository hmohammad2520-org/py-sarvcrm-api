from ._base import SarvModule
from ._mixins import UrlMixin

class AsolProject(SarvModule, UrlMixin):
    _module_name = 'asol_Project'
    _label_en = 'Project'
    _label_pr = 'پروژه'