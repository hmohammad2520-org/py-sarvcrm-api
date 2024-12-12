from sarvcrm_api.type_hints import SarvGetMethods

class SarvModule:
    _module_name = ''
    _label_en = 'BASE_CLASS'
    _label_pr = 'کلاس اصلی'

    def __init__(self, _client):
        from sarvcrm_api import SarvClient
        self._client: SarvClient = _client

    def create_get_parms(self, method:SarvGetMethods, **addition) -> dict:
        return self._client.create_get_parms(method, self, **addition)


    def create(self, **KWArgs) -> str:
        return self._client.send_request(
            request_method='POST',
            get_parms=self.create_get_parms('Save'),
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
            'offset': offset
        }
        post_parms = {k: v for k, v in post_parms.items() if v is not None}

        return self._client.send_request(
            request_method='POST',
            get_parms=self.create_get_parms('Retrieve'),
            post_parms=post_parms,
        ).get('data')


    def read_record(self, pk:str) -> dict:
        return self._client.send_request(
            request_method='GET',
            get_parms=self.create_get_parms('Retrieve', id=pk),
        ).get('data')[0]


    def update(self, pk:str, **KWArgs) -> str:
        return self._client.send_request(
            request_method = 'PUT',
            get_parms = self.create_get_parms('Save', id=pk),
            post_parms = KWArgs,
        ).get('id')


    def delete(self, pk:str) -> str | None:
        return self._client.send_request(
            request_method = 'DELETE',
            get_parms = self.create_get_parms('Save', id=pk),
        ).get('id', None)


    def get_module_fields(self) -> dict[str, dict]:
        return self._client.send_request(
            request_method='GET',
            get_parms=self.create_get_parms('GetModuleFields'),
        )

    def get_relationships(
            self,
            related_field:str,
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
            'offset': offset
        }
        post_parms = {k: v for k, v in post_parms.items() if v is not None}

        return self._client.send_request(
            request_method='POST',
            get_parms=self.create_get_parms('GetRelationship', related_field=related_field),
            post_parms=post_parms,
        )


    def save_relationships(
            self,
            pk:str,
            field_name:str,
            **related_records,
            ) -> list:
        
        return self._client.send_request(
            request_method='POST',
            get_parms=self.create_get_parms('SaveRelationships', id=pk),
            post_parms={'field_name': field_name, 'related_records': related_records},
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        return f'<SarvModule {self._label_en}>'