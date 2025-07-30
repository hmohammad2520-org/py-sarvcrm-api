from datetime import date, datetime
from typing import Dict, Set, Type


class BaseModel:
    id: str
    name: str
    created_by: str
    created_by_name: str
    date_entered: datetime
    modified_user_id: str
    modified_by_name: str
    date_modified: datetime
    deleted: bool

    _fields_names: Set[str] = set(
        [
            'id',
            'name',
            'created_by',
            'created_by_name',
            'date_entered',
            'modified_user_id',
            'modified_by_name',
            'date_modified',
            'deleted',
        ]
    )
    _casting: Dict[str, Type] = {
        'id': str,
        'name': str,
        'created_by': str,
        'created_by_name': str,
        'date_entered': datetime,
        'modified_user_id': str,
        'modified_by_name': str,
        'date_modified': datetime,
        'deleted': bool,
    }
    _sarv_type_map: Dict[str, Type] = {
        'id': str,
        'varchar': str,
        'text': str,
        'int': int,
        'integer': int,
        'float': float,
        'bool': bool,
        'date': date,
        'datetime': datetime,
    }

    @classmethod
    def _init_fields(cls, module) -> None:
        from sarvcrm_api import SarvModule
        cls.module: SarvModule = module

        if hasattr(module, 'get_module_fields'):
            fields = cls.module.get_module_fields()
            [cls._fields_names.add(field) for field in fields.keys()]

    def __init__(
            self,
            client,
            **kwargs,
        ) -> None:
        from sarvcrm_api import SarvClient
        self._client: SarvClient = client

        if not self._fields_names:
            raise NotImplementedError(f'This model does support item creation')

        for key, value in kwargs:
            if not key in self._fields_names:
                raise ValueError(f'Unknown field: {key}')

            setattr(self, key, self._casting.get(key, str)(value))
        