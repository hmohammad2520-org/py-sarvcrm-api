from classmods import ENVMod
from requests import HTTPError
from sarvcrm_api import SarvClient, SarvException

def test_create_env():
    ENVMod.save_example()
    ENVMod.sync_env_file()
    ENVMod.load_dotenv()

def test_create_client():
    client = SarvClient(**ENVMod.load_args(SarvClient.__init__))
    assert client
    return client

def test_login():
    client = test_create_client()
    with client:
        assert client.login(), 'Excepted token from server'

def test_query_accounts():
    client = test_create_client()
    with client:
        assert client.Accounts.read_list(), 'Excepted data from server'

def test_query_by_number():
    client = test_create_client()
    with client:
        assert client.search_by_number('02145885'), 'Excepted data from server'

def test_url_generations():
    client = test_create_client()
    assert client.Accounts.get_url_detail_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_edit_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_list_view()

def test_logout():
    client = test_create_client()
    with client:
        assert client.logout() is None
        try: client.Accounts.read_list(limit=1)
        except (HTTPError, SarvException): return
        raise AssertionError('Excepted HTTPError or SarvException on data from server')

def test_caching():
    client = test_create_client()
    with client:
        client.enable_caching()
        base_contacts = client.Contacts.read_list_all(caching=True, expire_after=5)
        cached_contacts = client.Contacts.read_list_all(caching=True)

    assert base_contacts == cached_contacts, 'Cached Results are not the same as Base Results'

def test_users():
    client = test_create_client()
    with client:
        assert client.Users.read_list()

def test_acl_roles():
    client = test_create_client()
    with client:
        assert client.ACLRoles.read_list()