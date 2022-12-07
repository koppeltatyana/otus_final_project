from json import dumps

import requests
from allure_commons._allure import attach, step
from allure_commons.types import AttachmentType
from curlify import to_curl


class BaseApi:
    """
    Класс-обвязка для непосредственного взаимодействия с методами библиотеки requests
    """

    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url
        self.session = requests.Session()

    def _create_curl(self, response: requests.Response):
        """
        A method for generating cURL and saving a request and response from the server to a file

        :param response: Response from the server
        :return: Response from the server
        """
        try:
            attach(
                body=to_curl(response.request),
                attachment_type=AttachmentType.TEXT,
                name='request',
            )
        except Exception:
            pass
        try:
            attach(
                body=dumps(response.json(), ensure_ascii=False, indent=4),
                attachment_type=AttachmentType.JSON,
                name='response',
            )
        except Exception:
            pass
        return response

    @step('Отправка GET запроса на url - {url}')
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
        return self._create_curl(
            response=self.session.get(
                url=f'{self.api_base_url}/{url}',
                verify=False,
                headers=headers,
                auth=auth,
            )
        )

    @step('Отправка POST запроса на url - {url}')
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
        return self._create_curl(
            response=self.session.post(
                url=f'{self.api_base_url}/{url}',
                json=data if is_json else None,
                data=None if is_json else data,
                files=files,
                verify=False,
                headers=headers,
            )
        )

    @step('Отправка PUT запроса на url - {url}')
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
        return self._create_curl(
            response=self.session.put(
                url=f'{self.api_base_url}/{url}',
                json=data if is_json else None,
                data=None if is_json else data,
                files=files,
                verify=False,
                headers=headers,
            )
        )

    @step('Отправка PATCH запроса на url - {url}')
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
        return self._create_curl(
            response=self.session.patch(
                url=f'{self.api_base_url}/{url}',
                data=data,
                verify=False,
                headers=headers,
            )
        )

    @step('Отправка DELETE запроса на url - {url}')
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
        return self._create_curl(
            response=self.session.delete(
                url=f'{self.api_base_url}/{url}',
                json=data if is_json else None,
                data=None if is_json else data,
                verify=False,
                headers=headers,
            )
        )
