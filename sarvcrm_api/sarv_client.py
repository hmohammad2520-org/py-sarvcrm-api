import json, requests, hashlib
from typing import Callable, Literal, TypeAlias, Optional

from sarvcrm_api.exceptions import SarvException
from ._base import ApiRouteMixin

RequestMethod: TypeAlias = Literal['GET','POST','PUT','DELETE']
LanguageType: TypeAlias = Literal['fa_IR','en_US']

requests_method_map: dict[LanguageType, Callable] = {
    'GET': requests.get,
    'POST': requests.post,
    'PUT': requests.put,
    'DELETE': requests.delete,
}

class SarvClient(ApiRouteMixin):
    def __init__(
            self, 
            base_url: str,
            utype: str,
            username: str,
            password: str,
            login_type: Optional[str] = None, 
            language: LanguageType = 'en_US',
            is_password_md5: bool = False,
            ) -> None:
        """Initialize the SarvClient."""

        self.base_url = base_url
        self.utype = utype
        self.username = username
        self.login_type = login_type
        self.language = language

        if is_password_md5 == True:
            self.password = password
        else:
            md5_hash = hashlib.md5(password.encode())
            self.password = md5_hash.hexdigest()

        self.token: str = ''

        super().__init__()

    def send_request(
            self, 
            method: RequestMethod, 
            head_parms: dict = None,
            get_parms: dict = None,
            post_parms: dict = None,
            ) -> dict:
        """Send a request to the Sarv API."""

        head_parms = head_parms or {}
        get_parms = get_parms or {}
        post_parms = post_parms or {}

        head_parms['Content-Type'] = 'application/json'
        head_parms['Authorization'] = f'Bearer {self.token}' if self.token else ''

        requests_method = requests_method_map.get(method, None)

        response:requests.Response = requests_method(
            url = self.base_url,
            params= get_parms,
            headers = head_parms, 
            data = post_parms,
            verify = True,
            )

        # Check for Server respond
        if 200 <= response.status_code < 500:
            # Deserialize sarvcrm servers response
            response_json = response.text
            response_dict: dict = json.loads(response_json)

        else:
            # Raise on server side http error
            response.raise_for_status()

        # Initiate server response
        if 200 <= response.status_code < 300:
            # return on clean server responses
            data = response_dict.get('data', {})
            return data

        elif 300 <= response.status_code < 400:
            raise SarvException(
                f"Redirection Response: {response.status_code} - {response_dict.get('message', 'Unknown error')}"
            )

        else:
            raise SarvException(
                f"{response.status_code} - {response_dict.get('message', 'Unknown error')}"
            )

    def login(self) -> str:
        """Authenticate the user and retrieve a token."""

        get_parms = {'method': 'login'}
        post_parms = {
            'utype': self.utype,
            'username': self.username,
            'password': self.password,
            'login_type': self.login_type,
            'language': self.language,
            }

        data = self.send_request(method='POST', get_parms=get_parms, post_parms=post_parms)
        if data:
            self.token = data.get('token')

        return self.token