import os, dotenv
from requests import HTTPError
from sarvcrm_api import SarvClient, SarvException, SarvURL

dotenv.load_dotenv()

client = SarvClient(
    SarvURL,
    os.environ.get('SARVCRM_UTYPE', ''),
    os.environ.get('SARVCRM_USERNAME', ''),
    os.environ.get('SARVCRM_PASSWORD', ''),
    is_password_md5=bool(os.environ.get('SARVCRM_PASS_MD5', False)),
)

def test_login():
    with client:
        assert client.login(), 'Excepted token from server'

def test_query_accounts():
    with client:
        assert client.Accounts.read_list(), 'Excepted data from server'

def test_query_by_number():
    with client:
        assert client.search_by_number('02145885'), 'Excepted data from server'

def test_url_generations():
    assert client.Accounts.get_url_detail_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_edit_view('ANY_PK_IS_ACCEPTABLE')
    assert client.Accounts.get_url_list_view()

def test_logout():
    with client:
        assert client.logout() is None
        try: client.Accounts.read_list(limit=1)
        except (HTTPError, SarvException): return
        raise AssertionError('Excepted HTTPError or SarvException on data from server')

def test_caching():
    with client:
        client.enable_caching()
        base_contacts = client.Contacts.read_list_all(caching=True, expire_after=5)
        cached_contacts = client.Contacts.read_list_all(caching=True)

    assert base_contacts == cached_contacts, 'Cached Results are not the same as Base Results'

def test_users():
    with client:
        assert client.Users.read_list()

def test_acl_roles():
    with client:
        assert client.ACLRoles.read_list()