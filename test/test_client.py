import os, dotenv
from sarvcrm_api import SarvClient, SarvURL

dotenv.load_dotenv()

sarv_client = SarvClient(
    SarvURL,
    os.environ.get('SARVCRM_UTYPE', ''),
    os.environ.get('SARVCRM_USERNAME', ''),
    os.environ.get('SARVCRM_PASSWORD', ''),
    is_password_md5=bool(os.environ.get('SARVCRM_PASS_MD5', False))
)

def test_login():
    assert sarv_client.login()

def test_query_accounts():
    assert sarv_client.Accounts.read_list()

def test_query_by_number():
    assert sarv_client.search_by_number('02145885')

def test_logout():
    assert sarv_client.logout() is None