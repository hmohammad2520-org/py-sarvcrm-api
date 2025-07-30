from typing import Any
from ._base import BaseModel

class Task(BaseModel):
    field_list = ['id', 'date_entered', 'date_modified', 'created_by', 'created_by_name', 'modified_user_id', 'modified_by_name', 'assigned_user_id', 'assigned_user_name', 'description', 'deleted', 'origin', 'name', 'status', 'duration_hours', 'duration_minutes', 'date_due_flag', 'date_due', 'time_due', 'date_due_field', 'date_start_flag', 'date_start', 'date_start_field', 'reminder_time', 'sms_reminder_time', 'parent_type', 'parent_name', 'parent_id', 'contact_id', 'contact_name', 'contact_phone', 'contact_email', 'priority', 'security_groups_id', 'security_groups_name', 'google_event_id', 'attachments', 'tasks_type']

    def __init__(self, **kwargs: Any) -> None:
        self.kwargs = kwargs
        self.init_custom_fields()

        for key, value in kwargs.items():
            if not key in self.field_list:
                raise ValueError(f"Invalid field: {key}")

            setattr(self, key, value)
    
        super().__init__(**kwargs)

        
    def init_custom_fields(self):
        pass