import os, dotenv
from sarvcrm_api import SarvClient, SarvURL

dotenv.load_dotenv()

client = SarvClient(
    SarvURL,
    os.environ.get('SARVCRM_UTYPE', ''),
    os.environ.get('SARVCRM_USERNAME', ''),
    os.environ.get('SARVCRM_PASSWORD', ''),
    is_password_md5=bool(os.environ.get('SARVCRM_PASS_MD5', False))
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

def test_logout():
    with client:
        assert client.logout() is None
        try: test_query_by_number(); return
        except AssertionError: ...
        raise AssertionError('Excepted assertion error on data call')