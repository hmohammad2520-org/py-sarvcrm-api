import requests
from typing import Literal, TypeAlias
from ._base import ApiRouteMixin

RequestMethod: TypeAlias = Literal['GET','POST','PUT','DELETE']
LanguageType: TypeAlias = Literal['fa_IR','en_US']

class SarvClient(ApiRouteMixin):
    def __init__(self, base_url:str, username:str, password:str, utype:str, login_type:str = None, language:LanguageType = 'fa_IR') -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.utype = utype
        self.login_type = login_type
        self.language = language

        self.token = self.Login()

        return super().__init__()

    def Send_Request(
            self, 
            method: RequestMethod, 
            header_parameters: dict = None, 
            get_parameters: dict = None, 
            post_parameters: dict = None
            ) -> dict:
        ...

    def Login(self) -> str:
        ...
