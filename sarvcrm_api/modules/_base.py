from sarvcrm_api import SarvClient
from sarvcrm_api.type_hints import SarvGetMethods

class SarvModule:
    _module_name = ''
    _label_en = 'BASE_CLASS'
    _label_pr = 'کلاس اصلی'

    def __init__(self, _client):
        self._client: SarvClient = _client

    def _create_get_parms(self,method:SarvGetMethods) -> dict:
        return {
            'method': method,
            'module': self._module_name
        }

    def create(self, **KWArgs) -> str:
        return self._client.send_request(
            method='POST',
            get_parms=self._create_get_parms('Save'),
            post_parms=KWArgs,
        ).get('id', {})

    def read_list(
            self,
            query:str = None,
            order_by:str = None,
            select_fields:list[str] = None,
            limit:int = None,
            offset: int = None,
            ) -> list:

        post_parms = {
            'query': query,
            'order_by': order_by,
            'select_fields': select_fields,
            'limit': limit,
            'offset': offset,
        }

        return self._client.send_request(
            method='POST',
            get_parms=self._create_get_parms('Retrieve'),
            post_parms=post_parms,
        ).get('data')


    def read_record(self, pk:str) -> dict:
        get_parms = self._create_get_parms('Retrieve')
        get_parms['id'] = pk

        return self._client.send_request(
            method='GET',
            get_parms=get_parms,
        ).get('data')[0]


    def update(self, pk:str, **KWArgs) -> str:
        get_parms = self._create_get_parms('Save')
        get_parms['id'] = pk

        return self._client.send_request(
            method='PUT',
            get_parms=get_parms,
            post_parms=KWArgs,
        ).get('id')

    def delete(self, pk:str) -> str | None:
        get_parms = self._create_get_parms('Save')
        get_parms['id'] = pk

        return self._client.send_request(
            method='DELETE',
            get_parms=get_parms,
        ).get('id', None)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        return f'<SarvModule {self._label_en}>'