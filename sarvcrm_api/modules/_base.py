from sarvcrm_api.type_hints import SarvGetMethods

class SarvModule:
    _module_name = ''
    _label_en = 'BASE_CLASS'
    _label_pr = 'کلاس اصلی'

    def __init__(self, _client):
        """Initiate the Module class and set the clinet as a local varible"""
        from sarvcrm_api import SarvClient
        self._client: SarvClient = _client


    def create_get_parms(
            self,
            sarv_get_method:SarvGetMethods,
            **addition
            ) -> dict:
        """Create the get parameter with the method and module"""

        return self._client.create_get_parms(sarv_get_method, self, **addition)


    def create(self, **KWArgs) -> str:
        """Creates the item in the module"""

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
        """Returns a list of items"""

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
        """Returns item from id of the item"""

        return self._client.send_request(
            request_method='GET',
            get_parms=self.create_get_parms('Retrieve', id=pk),
        ).get('data')[0]


    def update(self, pk:str, **fields_data) -> str:
        """Updates the fields from id of the item"""

        return self._client.send_request(
            request_method = 'PUT',
            get_parms = self.create_get_parms('Save', id=pk),
            post_parms = fields_data,
        ).get('id')


    def delete(self, pk:str) -> str | None:
        """Deletes the item with id"""

        return self._client.send_request(
            request_method = 'DELETE',
            get_parms = self.create_get_parms('Save', id=pk),
        ).get('id')


    def get_module_fields(self) -> dict[str, dict]:
        """Gets all of the fields of a module"""

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
        """returns list of items in relationship of the related field"""

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
            related_records:list,
            ) -> list:
        """Saves the relationship"""

        return self._client.send_request(
            request_method='POST',
            get_parms=self.create_get_parms('SaveRelationships', id=pk),
            post_parms={'field_name': field_name, 'related_records': related_records},
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        return f'<SarvModule {self._label_en}>'