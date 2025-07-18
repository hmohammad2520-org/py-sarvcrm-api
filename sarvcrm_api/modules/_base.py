from typing import Any, Optional
from sarvcrm_api._type_hints import SarvGetMethods

BASE_LIMIT = 300
BASE_OFFSET = 0

class SarvModule:
    """
    A base class for interacting with a Sarv CRM module. This class provides methods to 
    create, read, update, delete, and manage relationships of records in a module.
    
    Attributes:
        _module_name (str): The name of the module.
        _label_en (str): The label of the module in English.
        _label_pr (str): The label of the module in Persian.
        _client (SarvClient): The client instance used to send requests to the Sarv CRM API.
    """
    _module_name: str = ''
    _label_en: str = 'BASE_CLASS'
    _label_pr: str = 'کلاس اصلی'

    def __init__(self, _client):
        """
        Initializes the SarvModule instance with a given client.

        Args:
            _client (SarvClient): The client used for making API requests to Sarv CRM.
        """
        from sarvcrm_api import SarvClient
        self._client: SarvClient = _client

    def _create_get_params(self, sarv_get_method: SarvGetMethods, **addition) -> dict:
        """
        Constructs the parameters for a 'GET' request based on the provided method and additional parameters.

        Args:
            sarv_get_method (SarvGetMethods): The specific 'GET' method to retrieve data.
            **addition: Additional parameters to customize the request.

        Returns:
            dict: The parameters to be used in the GET request.
        """
        return self._client._create_get_params(sarv_get_method, self, **addition)

    def create(self, **fields_data) -> str:
        """
        Creates a new item in the module with the provided field values.

        Args:
            **fields_data: The fields and values to be used in the creation of the item.

        Returns:
            str: The ID of the newly created item.
        """
        return self._client._send_request(
            request_method='POST',
            get_params=self._create_get_params('Save'),
            post_params=fields_data,
        ).get('id', {})

    def read_list(
            self,
            query: Optional[str] = None,
            order_by: Optional[str] = None,
            select_fields: Optional[list[str]] = None,
            limit: int = BASE_LIMIT,
            offset: int = BASE_OFFSET,
            caching: bool = False,
            expire_after: int = 300,
        ) -> list[dict]:
        """
        Retrieves a list of items from the module, optionally filtered by the specified parameters.

        Args:
            query (str, optional): A query to filter the results.
            order_by (str, optional): A field to order the results by.
            select_fields (list[str], optional): A list of fields to include in the response.
            limit (int): The maximum number of items to retrieve.
            offset (int): The number of items to skip before starting to return results.

        Returns:
            list: A list of items from the module.
        """
        post_params = {
            'query': query,
            'order_by': order_by,
            'select_fields': select_fields,
            'limit': limit,
            'offset': offset
        }

        post_params = {k: v for k, v in post_params.items() if v is not None}

        return self._client._send_request(
            request_method='POST',
            get_params=self._create_get_params('Retrieve'),
            post_params=post_params,
            caching=caching,
            expire_after=expire_after,
        )

    def read_list_all(
            self,
            query: Optional[str] = None,
            order_by: Optional[str] = None,
            select_fields: Optional[list[str]] = None,
            item_buffer: int = BASE_LIMIT,
            caching: bool = False,
            expire_after: int = 300,
        ) -> list[dict]:
        """
        Retrieves all of items from the module, optionally filtered by the specified parameters.

        Args:
            query (str, optional): A query to filter the results.
            order_by (str, optional): A field to order the results by.
            select_fields (list[str], optional): A list of fields to include in the response.
            item_buffer (int): Number of items to query each iteration from sarv server.

        Returns:
            list: A list of all items from the module.
        """
        offset = 0
        all_list = []
        new = ['']
        while new:
            new = self.read_list(
                query=query, 
                order_by=order_by, 
                select_fields=select_fields,
                limit=item_buffer,
                offset=offset,
                caching=caching,
                expire_after=expire_after,
            )
            all_list += new
            offset += item_buffer

        return all_list

    def read_record(self, pk: str) -> dict[str, Any]:
        """
        Retrieves a single item from the module using its unique identifier (ID).

        Args:
            pk (str): The unique identifier (ID) of the item to retrieve.

        Returns:
            dict: The data of the retrieved item.
        """
        return self._client._send_request(
            request_method='GET',
            get_params=self._create_get_params('Retrieve', id=pk),
        )[0]

    def update(self, pk: str, **fields_data) -> str:
        """
        Updates an existing item in the module with the given field values.

        Args:
            pk (str): The unique identifier (ID) of the item to update.
            **fields_data: The fields and values to update in the item.

        Returns:
            str: The ID of the updated item.
        """
        return self._client._send_request(
            request_method='PUT',
            get_params=self._create_get_params('Save', id=pk),
            post_params=fields_data,
        ).get('id')

    def delete(self, pk: str) -> str | None:
        """
        Deletes an item from the module using its unique identifier (ID).

        Args:
            pk (str): The unique identifier (ID) of the item to delete.

        Returns:
            str | None: The ID of the deleted item or None if no item was deleted.
        """
        return self._client._send_request(
            request_method='DELETE',
            get_params=self._create_get_params('Save', id=pk),
        ).get('id')

    def get_module_fields(
            self,
            caching: bool = False,
            expire_after: int = 300,
        ) -> dict[str, dict]:
        """
        Retrieves the list of all fields for the module.

        Returns:
            dict: A dictionary containing all the fields of the module.
        """
        return self._client._send_request(
            request_method='GET',
            get_params=self._create_get_params('GetModuleFields'),
            caching=caching,
            expire_after=expire_after,
        )

    def get_relationships(
            self,
            related_field: str,
            query: Optional[str] = None,
            order_by: Optional[str] = None,
            select_fields: Optional[list[str]] = None,
            limit: int = BASE_OFFSET,
            offset: int = BASE_LIMIT,
            caching: bool = False,
            expire_after: int = 300,
        ) -> list:
        """
        Retrieves a list of related items for a specific field in the module.

        Args:
            related_field (str): The related field to fetch relationships for.
            query (str, optional): A query to filter the results.
            order_by (str, optional): A field to order the results by.
            select_fields (list[str], optional): A list of fields to include in the response.
            limit (int): The maximum number of items to retrieve.
            offset (int): The number of items to skip before starting to return results.

        Returns:
            list: A list of related items.
        """
        post_params = {
            'query': query,
            'order_by': order_by,
            'select_fields': select_fields,
            'limit': limit,
            'offset': offset
        }
        post_params = {k: v for k, v in post_params.items() if v is not None}

        return self._client._send_request(
            request_method='POST',
            get_params=self._create_get_params('GetRelationship', related_field=related_field),
            post_params=post_params,
            caching=caching,
            expire_after=expire_after,
        )

    def save_relationships(
            self,
            pk: str,
            field_name: str,
            related_records: list,
        ) -> list:
        """
        Saves a relationship between the current item and related records.

        Args:
            pk (str): The unique identifier (ID) of the item.
            field_name (str): The name of the field to establish the relationship.
            related_records (list): A list of related records to associate with the item.

        Returns:
            list: A list of the related records saved in the relationship.
        """
        return self._client._send_request(
            request_method='POST',
            get_params=self._create_get_params('SaveRelationships', id=pk),
            post_params={'field_name': field_name, 'related_records': related_records},
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the SarvModule instance.

        Returns:
            str: A string representation of the SarvModule instance.
        """
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        """
        Returns a string that describes the SarvModule instance.

        Returns:
            str: A description of the SarvModule instance.
        """
        return f'<SarvModule {self._label_en}>'
