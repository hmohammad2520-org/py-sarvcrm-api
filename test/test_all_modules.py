from classmods import ENVMod
from requests import HTTPError
from sarvcrm_api import SarvClient, SarvModule, SarvException


client = None


def create_client():
    global client
    if client is None:
        ENVMod.load_dotenv()
        client = SarvClient(**ENVMod.load_args(SarvClient.__init__))

    assert client
    return client

def test_all_modules():
    client = create_client()
    for module in client.__dict__.values():
        if isinstance(module, SarvModule):
            module.read_list(limit=1)
            module.read_all(query='FALSE')
            module.read_user_created()
