from classmods import ENVMod
from sarvcrm_api import SarvClient
from sarvcrm_api.models import Account

ENVMod.load_dotenv()

def test_create_client():
    client = SarvClient(**ENVMod.load_args(SarvClient.__init__))
    assert client
    return client

def test_model_creation():
    client = test_create_client()
    with client:
        random_id = client.Accounts.read_list(selected_fields=['id'], offset=110, limit=1)[0]['id']
        my_account = Account.get(random_id)
        fields = Account._fields
        assert my_account
        assert fields
