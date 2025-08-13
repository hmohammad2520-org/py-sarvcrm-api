from ._base import SarvModule
from ._mixins import UrlMixin
from ..models.notification import Notification

class Notifications(SarvModule, UrlMixin):
    _module_name = 'Notifications'
    _table_name = 'notifications'
    _assigned_field = 'assigned_user_id'
    _label_en = 'Notifications'
    _label_pr = 'نوتیفیکیشن'
    _item_class = Notification