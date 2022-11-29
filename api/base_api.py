from requests import get, delete, patch, post, put


class BaseApi:
    """
    Класс-обвязка для непосредственного взаимодействия с методами библиотеки requests
    """

    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url

    def _get(self, url='/', headers=None, auth=None):
        """
        Method for sending a GET request to the server

        :param url: Request URL
        :param headers: Request headers
        :param auth: Basic authorization on the server
        :return: Response in JSON format
        """
        if headers is None:
            headers = {}
        if auth is None:
            auth = ()
        return get(
            url=f'{self.api_base_url}/{url}',
            verify=False,
            headers=headers,
            auth=auth,
        )

    def _post(self, data=None, url='/', is_json=False, files=None, headers=None):
        """
        Method for sending a POST request to the server

        :param data: Body in JSON format
        :param url: Request URL
        :param is_json: The parameter controlling the Content-Type header
        :param files: Uploading files
        :param headers: Request headers
        :return: Response in JSON format
        """
        if files is None:
            files = {}
        if headers is None:
            headers = {}
        return post(
            url=f'{self.api_base_url}/{url}',
            json=data if is_json else None,
            data=None if is_json else data,
            files=files,
            verify=False,
            headers=headers,
        )

    def _put(self, data=None, url='/', is_json=False, files=None, headers=None):
        """
        Method for sending a PUT request to the server

        :param data: Body in JSON format
        :param url: Request URL
        :param is_json: The parameter controlling the Content-Type header
        :param files: Uploading files
        :param headers: Request headers
        :return: Response in JSON format
        """
        if files is None:
            files = {}
        if headers is None:
            headers = {}
        return put(
            url=f'{self.api_base_url}/{url}',
            json=data if is_json else None,
            data=None if is_json else data,
            files=files,
            verify=False,
            headers=headers,
        )

    def _patch(self, url='/', data=None, headers=None):
        """
        Method for sending a PATCH request to the server

        :param url: Request URL
        :param data: Body in JSON format
        :param headers: Request headers
        :return: Response in JSON format
        """
        if headers is None:
            headers = {}
        return patch(
            url=f'{self.api_base_url}/{url}',
            data=data,
            verify=False,
            headers=headers,
        )

    def _delete(self, data=None, url='/', headers=None):
        """
        Method for sending a DELETE request to the server

        :param data: Body in JSON format
        :param url: Request URL
        :param headers: Request headers
        :return: Response in JSON format
        """
        is_json = True if isinstance(data, dict) else False
        if headers is None:
            headers = {}
        return delete(
            url=f'{self.api_base_url}/{url}',
            json=data if is_json else None,
            data=None if is_json else data,
            verify=False,
            headers=headers,
        )
