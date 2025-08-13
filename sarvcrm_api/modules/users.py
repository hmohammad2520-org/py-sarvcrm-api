from ._base import SarvModule
from ._mixins import UrlMixin

class Users(SarvModule, UrlMixin):
    _module_name = 'Users'
    _label_en = 'Users'
    _label_pr = 'کاربران'

    def get_me(self) -> dict:
        return self.read_list(
            query=f"users.user_name='{self._client._username.lower()}'",
            limit=1,
        )[0]