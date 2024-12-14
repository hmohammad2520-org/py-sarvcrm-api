from typing import TypeAlias, Union, List
from uuid import UUID
from decimal import Decimal
from datetime import date, datetime

from ._base import SarvFieldType

class Linkable(SarvFieldType):
    _field_type_name: str = 'Linkable'
    _alias: TypeAlias = None


class AssignedUserName(SarvFieldType):
    _field_type_name: str = 'assigned_user_name'
    _alias: TypeAlias = None


class Base(SarvFieldType):
    _field_type_name: str = 'base'
    _alias: TypeAlias = None


class Bool(SarvFieldType):
    _field_type_name: str = 'bool'
    _alias: TypeAlias = None


class Boolean(SarvFieldType):
    _field_type_name: str = 'boolean'
    _alias: TypeAlias = None


class Char(SarvFieldType):
    _field_type_name: str = 'char'
    _alias: TypeAlias = None


class Currency(SarvFieldType):
    _field_type_name: str = 'currency'
    _alias: TypeAlias = None


class Date(SarvFieldType):
    _field_type_name: str = 'date'
    _alias: TypeAlias = None


class Datetime(SarvFieldType):
    _field_type_name: str = 'datetime'
    _alias: TypeAlias = None


class Datetimecombo(SarvFieldType):
    _field_type_name: str = 'datetimecombo'
    _alias: TypeAlias = None


class Decimal(SarvFieldType):
    _field_type_name: str = 'decimal'
    _alias: TypeAlias = None


class Durationcombo(SarvFieldType):
    _field_type_name: str = 'durationcombo'
    _alias: TypeAlias = None


class Email(SarvFieldType):
    _field_type_name: str = 'email'
    _alias: TypeAlias = None


class Enum(SarvFieldType):
    _field_type_name: str = 'enum'
    _alias: TypeAlias = None


class File(SarvFieldType):
    _field_type_name: str = 'file'
    _alias: TypeAlias = None


class Fullname(SarvFieldType):
    _field_type_name: str = 'fullname'
    _alias: TypeAlias = None


class Function(SarvFieldType):
    _field_type_name: str = 'function'
    _alias: TypeAlias = None


class Id(SarvFieldType):
    _field_type_name: str = 'id'
    _alias: TypeAlias = None


class Int(SarvFieldType):
    _field_type_name: str = 'int'
    _alias: TypeAlias = None


class Integer(SarvFieldType):
    _field_type_name: str = 'integer'
    _alias: TypeAlias = None


class Linkable(SarvFieldType):
    _field_type_name: str = 'linkable'
    _alias: TypeAlias = None


class Multienum(SarvFieldType):
    _field_type_name: str = 'multienum'
    _alias: TypeAlias = None


class Name(SarvFieldType):
    _field_type_name: str = 'name'
    _alias: TypeAlias = None


class Parent(SarvFieldType):
    _field_type_name: str = 'parent'
    _alias: TypeAlias = None


class ParentType(SarvFieldType):
    _field_type_name: str = 'parent_type'
    _alias: TypeAlias = None


class Phone(SarvFieldType):
    _field_type_name: str = 'phone'
    _alias: TypeAlias = None


class Relate(SarvFieldType):
    _field_type_name: str = 'relate'
    _alias: TypeAlias = None


class Text(SarvFieldType):
    _field_type_name: str = 'text'
    _alias: TypeAlias = None


class Tinyinit(SarvFieldType):
    _field_type_name: str = 'tinyinit'
    _alias: TypeAlias = None


class Tree(SarvFieldType):
    _field_type_name: str = 'tree'
    _alias: TypeAlias = None


class Varchar(SarvFieldType):
    _field_type_name: str = 'varchar'
    _alias: TypeAlias = None
