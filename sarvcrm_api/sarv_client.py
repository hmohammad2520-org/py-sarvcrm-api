import json, requests, hashlib
from typing import Callable, Optional

from .exceptions import SarvException
from ._base import ModulesMixin
from .type_hints import SarvLanguageType, RequestMethod, SarvGetMethods

from .modules._base import SarvModule

requests_method_map: dict[SarvLanguageType, Callable] = {
    'GET': requests.get,
    'POST': requests.post,
    'PUT': requests.put,
    'DELETE': requests.delete,
}

class SarvClient(ModulesMixin):
    def __init__(
            self, 
            base_url: str,
            utype: str,
            username: str,
            password: str,
            login_type: Optional[str] = None, 
            language: SarvLanguageType = 'en_US',
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
            self.password  = hashlib.md5(password.encode('utf-8')).hexdigest()

        self.token: str = ''

        super().__init__()


    def create_get_parms(
            self, 
            sarv_get_method: SarvGetMethods = None,
            sarv_module: SarvModule | str = None,
            **addition
            ) -> dict:

        module_name = None

        if sarv_module is not None:
            if isinstance(sarv_module,SarvModule):
                module_name = sarv_module._module_name
            elif isinstance(sarv_module,str):
                module_name = sarv_module
            else:
                raise TypeError(f'Module type must be instance of SarvModule or str not {sarv_module.__class__.__name__}')
        
        get_parms = {}
        
        if sarv_get_method is not None:
            get_parms['method'] = sarv_get_method

        if module_name is not None:
            get_parms['module'] = module_name

        if addition:
            get_parms.update(**addition)

        return get_parms


    def send_request(
            self, 
            request_method: RequestMethod, 
            head_parms: dict = None,
            get_parms: dict = None,
            post_parms: dict = None,
            ) -> dict:
        """Send a request to the Sarv API and returns the data parameter of the response"""

        requests_method = requests_method_map.get(request_method, None)

        head_parms = head_parms or {}
        get_parms = get_parms or {}
        post_parms = post_parms or {}

        head_parms['Content-Type'] = 'application/json'

        if self.token:
            head_parms['Authorization'] = f'Bearer {self.token}'

        if not requests_method:
            raise TypeError(f'This request method is not valid http method: {request_method}')

        response:requests.Response = requests_method(
            url = self.base_url,
            params = get_parms,
            headers = head_parms, 
            json = post_parms,
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

        post_parms = {
            'utype': self.utype,
            'user_name': self.username,
            'password': self.password,
            'login_type': self.login_type,
            'language': self.language,
            }

        data = self.send_request(
            request_method='POST', 
            get_parms=self.create_get_parms('Login'), 
            post_parms=post_parms,
            )
        if data:
            self.token = data.get('token')

        return self.token
    

    def logout(self) -> None:
        """Clears token from the instance"""
        if self.token:
            self.token = ''


    def search_by_number(
            self,
            number:str,
            module: Optional[SarvModule | str] = None
            ) -> None:
        """Searches the crm by phone number and retrives the module item"""

        return self.send_request(
            request_method='GET',
            get_parms=self.create_get_parms('SearchByNumber', sarv_module=module, number=number),
            )


    def __repr__(self):
        return f'{self.__class__.__name__}(utype={self.utype}, username={self.username})'


    def __str__(self) -> str:
        return f'<SarvClient {self.utype}>'
