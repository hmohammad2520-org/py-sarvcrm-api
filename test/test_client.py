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

# must be first
def test_login():
    with client:
        assert client.login()


def test_query_accounts():
    with client:
        assert client.Accounts.read_list()

def test_query_by_number():
    with client:
        assert client.search_by_number('02145885')


# must be at the end
def test_logout():
    with client:
        assert client.logout() is None