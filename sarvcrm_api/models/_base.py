from datetime import date, datetime
from typing import Any, Callable, Dict, List, Self, Type, Optional, Union
from .._exceptions import SarvServerErrors


class FieldMeta:
    def __init__(
            self, 
            name: str,
            label: str,
            type: str,
            default_value: Optional[Any] = None,
            id_name: Optional[str] = None,
            group: Optional[str] = None,
            len: Optional[str] = None,
            options: Optional[List[Dict[str, str]]] = None,
            related_module: Optional[str] = None,
            calculated: Optional[str] = None,
            required: Optional[int] = None,
        ) -> None:

        self.name = name
        self.label = label
        self.type = type
        self.default_value = default_value
        self.id_name = id_name or None
        self.group = group or None
        self.len = int(len) if len else 0
        self.options = options or []
        self.related_module = related_module or None
        self.calculated = calculated
        self.required = bool(required)

        self._normal_type: Optional[Type] = None

    @staticmethod
    def _cast(callable: Callable[[str|list|dict], Any]) -> Any:
        ...

class SarvModel:
    id: str
    _fields: Dict[str, FieldMeta] = {}
    _base_fields: List[str] = [
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
    _casting: Dict[str, Type] = {
        'id': str,
        'name': str,
        'created_by': str,
        'created_by_name': str,
        'date_entered': str,
        'modified_user_id': str,
        'modified_by_name': str,
        'date_modified': str,
        'deleted': bool,
    }
    _sarv_type_map: Dict[str, Type] = {
        'id': str,
        'varchar': str,
        'text': str,
        'int': str,
        'integer': int,
        'float': str,
        'bool': str,
        'date': str,
        'datetime': str,
    }

    @classmethod
    def _init_module(cls, module) -> None:
        from sarvcrm_api import SarvModule
        cls.module: SarvModule = module

    @classmethod
    def _init_fields(cls) -> None:
        if not cls._fields and hasattr(cls.module, 'get_module_fields'):
            for field, meta in cls.module.get_module_fields().items():
                cls._fields[field] = FieldMeta(**meta)

    def __init__(
            self,
            _override_required: bool = False,
            **kwargs: Any
        ) -> None:

        if not self._fields:
            self._init_fields()

        for key in kwargs:
            if key not in self._fields:
                raise ValueError(f'[{self.__class__.__name__}] Unknown field: {key}')

        for field, meta in self._fields.items():
            raw_value = kwargs.get(field)
            
            if not _override_required and meta.required and raw_value is None:
                if not field == 'id':
                    raise SarvServerErrors.RequiredField(f'This field is required: {field}')

            cast_func = self._casting.get(field, str)

            try:
                value = cast_func(raw_value) if raw_value is not None else None

            except Exception as e:
                raise ValueError(f"[{field}] Failed casting '{raw_value}' to {cast_func.__name__}: {e}")

            setattr(self, field, value)

    @classmethod
    def get(cls, uid: str) -> Self:
        data = cls.module.read_record(uid)
        if data:
            return cls(_override_required=True, **data)

        raise SarvServerErrors.ItemNotFound(f'Item with id not found: {uid}')

    @classmethod
    def query(cls, **filters) -> List[Self]:
        if filters:
            query_str = " AND ".join(f"{key}='{value}'" for key, value in filters.items())

        else:
            query_str = None

        raw_items = cls.module.read_list(
            query = query_str
        )
        return [cls(_override_required=True, **item) for item in raw_items]

    @classmethod
    def all(cls) -> List[Self]:
        raw_items = cls.module.read_list_all()
        return [cls(**item) for item in raw_items]

    def to_dict(self) -> Dict[str, Any]:
        return {field: getattr(self, field, None) for field in self._fields}

    def save(self) -> Self:
        data = self.to_dict()
        if getattr(self, "id", None):
            response_id = self.module.update(self.id, **data)

        else:
            response_id = self.module.create(**data)
            self.id = response_id

        self = self.__class__.get(self.id)
        return self

    def delete(self) -> bool:
        if not getattr(self, "id", None):
            raise ValueError("Cannot delete without an 'id'")

        deleted_id = self.module.delete(self.id)
        return deleted_id == self.id


    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={getattr(self, 'id', None)}>"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.to_dict()})"
