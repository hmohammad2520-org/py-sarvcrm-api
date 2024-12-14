from typing import TypeAlias, Union, List
from uuid import UUID
from decimal import Decimal
from datetime import date, datetime

from ._base import SarvFieldType


class AssignedUserName(SarvFieldType):
    _field_type_name: str = 'assigned_user_name'
    _alias: TypeAlias = str


class Base(SarvFieldType):
    _field_type_name: str = 'base'
    _alias: TypeAlias = object


class Bool(SarvFieldType):
    _field_type_name: str = 'bool'
    _alias: TypeAlias = bool


class Boolean(SarvFieldType):
    _field_type_name: str = 'boolean'
    _alias: TypeAlias = bool


class Char(SarvFieldType):
    _field_type_name: str = 'char'
    _alias: TypeAlias = str


class Currency(SarvFieldType):
    _field_type_name: str = 'currency'
    _alias: TypeAlias = Decimal


class Date(SarvFieldType):
    _field_type_name: str = 'date'
    _alias: TypeAlias = date


class Datetime(SarvFieldType):
    _field_type_name: str = 'datetime'
    _alias: TypeAlias = datetime


class Datetimecombo(SarvFieldType):
    _field_type_name: str = 'datetimecombo'
    _alias: TypeAlias = datetime


class Decimal(SarvFieldType):
    _field_type_name: str = 'decimal'
    _alias: TypeAlias = Decimal


class Durationcombo(SarvFieldType):
    _field_type_name: str = 'durationcombo'
    _alias: TypeAlias = str


class Email(SarvFieldType):
    _field_type_name: str = 'email'
    _alias: TypeAlias = str


class Enum(SarvFieldType):
    _field_type_name: str = 'enum'
    _alias: TypeAlias = str


class File(SarvFieldType):
    _field_type_name: str = 'file'
    _alias: TypeAlias = str


class Fullname(SarvFieldType):
    _field_type_name: str = 'fullname'
    _alias: TypeAlias = str


class Function(SarvFieldType):
    _field_type_name: str = 'function'
    _alias: TypeAlias = callable


class Id(SarvFieldType):
    _field_type_name: str = 'id'
    _alias: TypeAlias = Union[UUID, str]


class Int(SarvFieldType):
    _field_type_name: str = 'int'
    _alias: TypeAlias = int


class Integer(SarvFieldType):
    _field_type_name: str = 'integer'
    _alias: TypeAlias = int


class Linkable(SarvFieldType):
    _field_type_name: str = 'linkable'
    _alias: TypeAlias = str


class Multienum(SarvFieldType):
    _field_type_name: str = 'multienum'
    _alias: TypeAlias = List[str]


class Name(SarvFieldType):
    _field_type_name: str = 'name'
    _alias: TypeAlias = str


class Parent(SarvFieldType):
    _field_type_name: str = 'parent'
    _alias: TypeAlias = Union[UUID, str]


class ParentType(SarvFieldType):
    _field_type_name: str = 'parent_type'
    _alias: TypeAlias = str


class Phone(SarvFieldType):
    _field_type_name: str = 'phone'
    _alias: TypeAlias = str


class Relate(SarvFieldType):
    _field_type_name: str = 'relate'
    _alias: TypeAlias = Union[str, UUID]


class Text(SarvFieldType):
    _field_type_name: str = 'text'
    _alias: TypeAlias = str


class Tinyinit(SarvFieldType):
    _field_type_name: str = 'tinyinit'
    _alias: TypeAlias = bool


class Tree(SarvFieldType):
    _field_type_name: str = 'tree'
    _alias: TypeAlias = object


class Varchar(SarvFieldType):
    _field_type_name: str = 'varchar'
    _alias: TypeAlias = str
