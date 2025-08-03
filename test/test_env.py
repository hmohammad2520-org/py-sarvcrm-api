from classmods import ENVMod
from sarvcrm_api import SarvClient as _

def test_create_env():
    ENVMod.save_example()
    ENVMod.sync_env_file()
