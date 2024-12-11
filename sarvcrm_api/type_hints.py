from typing import Literal, TypeAlias

RequestMethod: TypeAlias = Literal['GET','POST','PUT','DELETE']
SarvLanguageType: TypeAlias = Literal['fa_IR','en_US']
SarvGetMethods: TypeAlias = Literal[
    'Login',
    'Save',
    'Retrieve',
    'GetModuleFields',
    'GetRelationship',
    'SaveRelationships',
    'SearchByNumber',
    ]

__all__ = [
    'RequestMethod',
    'SarvLanguageType',
    'SarvGetMethods',
]