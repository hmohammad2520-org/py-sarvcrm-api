from typing import TypeAlias

class SarvFieldType:
    """
    A base class for interacting with a Sarv CRM field types.
    
    Attributes:
        _field_type_name (str): The name of the field type in sarvcrm.
        _alias (TypeAlias): Type equivalent in python types and typehints
    """

    _field_type_name: str = 'BaseField'
    _alias: TypeAlias = None


class SarvField:
    """
    A base class for interacting with a Sarv CRM fields.
    
    Attributes:
        _field_name (str): The name of the field in sarvcrm.
        _field_type (SarvFieldTypes): Field Type
    """

    _field_name: str = ''
    _field_type: 'SarvFieldType' = SarvFieldType
    