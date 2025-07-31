from typing import List
import __init__ as _
from classmods import ENVMod
from sarvcrm_api import SarvClient, SarvModule

template = '''
### This file is generated using Scripts ###
### Do not modify by any means ###

from ._base import BaseModel


class {class_name}(BaseModel):
    """
    This class represents single item in {module_name}.
    """
    {fields}
'''.strip()

ENVMod.load_dotenv()

client = SarvClient(**ENVMod.load_args(SarvClient.__init__))

modules: List[SarvModule] = []

with client:
    for attr, value in client.__dict__.items():
        if isinstance(value, SarvModule):
            print(f'Initiating: {value._item_class.__name__}')
            value._item_class._init_fields()
            modules.append(value)
            break

for module in modules:
    print(template.format(
        class_name = module._item_class.__name__,
        module_name = module.__class__.__name__,
        fields='    '.join([f'{(x.name+': str'):45}  # {x.group=}, {x.type=}\n' for _, x in module._item_class._fields.items() if x.name not in module._item_class._base_fields]),
        args='',
        )
    )
    break