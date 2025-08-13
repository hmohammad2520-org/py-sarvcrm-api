from classmods import ENVMod
from requests import HTTPError
from sarvcrm_api import SarvClient, SarvServerError


client = None


def create_client():
    global client
    if client is None:
        ENVMod.load_dotenv()
        client = SarvClient(**ENVMod.load_args(SarvClient.__init__))

    assert client
    return client

def test_login():
    client = create_client()
    with client:
        assert client.login(), 'Excepted token from server'

def test_logout():
    client = create_client()
    with client:
        assert client.logout() is None
        setting = client._auto_login
        client._auto_login = False
        try: 
            client.Accounts.read_list(limit=1)

        except (HTTPError, SarvException):
            return

        finally:
            client._auto_login = setting

        raise AssertionError('Excepted HTTPError or SarvException on data from server')

def test_get_me():
    client = create_client()
    assert client.user_id

def test_auto_login():
    client = create_client()
    with client:
        assert client.logout() is None
        setting = client._auto_login
        client._auto_login = True
        assert client.Accounts.read_list(limit=1)
        client._auto_login = setting

def test_query_by_number():
    client = create_client()
    with client:
        assert client.search_by_number('02145885'), 'Excepted data from server'

def test_url_generations():
    client = create_client()
    assert client.Accounts.get_url_detail_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_edit_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_list_view()

def test_caching():
    client = create_client()
    with client:
        client.enable_caching()
        base_contacts = client.Contacts.read_all(caching=True, expire_after=5)
        cached_contacts = client.Contacts.read_all(caching=True)

    assert base_contacts == cached_contacts, 'Cached Results are not the same as Base Results'
