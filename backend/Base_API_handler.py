import json
from json import JSONDecodeError

import requests


class BaseAPI:
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json'}

    def __init__(self):
        self.base_url = 'http://192.168.1.254/api/'
        self.authentication = 'authentication'
        self.init_done = 'initialization'
        self.version = 'version'
        if self.get_initialization_status() == 'NotDone':
            self.patch_admin_password()
        else:
            self.authorize()

    def send_request(self, request_type: str, url: str, **kwargs) -> dict:
        """
        Wysłanie żądania do aplikacji po stronie API
        :param request_type: typ żądania, tj. 'post', 'put', 'get', 'patch' albo 'delete'
        :param url: ścieżka żądania, która będzie dodana do podstawowej ścieżki
        :return: Słownik z wartością zwróconą
        """
        call = getattr(requests, request_type)
        try:
            response = call(self.base_url + url, headers=BaseAPI.headers, **kwargs)
            if response.status_code not in [200, 201, 202]:
                raise ValueError(response.json())
            return response.json()
        except JSONDecodeError:
            if response.reason == 'No Content' or response.reason == 'OK':
                return response
            else:
                raise ValueError(f'Response code error: {response.status_code}, with reason: {response.reason}.')
        # if url != 'authentication' and :
        #     if response['status'] not in [200, 201, 202] and type(response['status']) == int:
        #         raise TypeError(response)

    def authorize(self):
        data = {
            "login": "Admin",
            "password": "Smartspaces1!",
            "tool": "Configuration"
        }
        data = json.dumps(data)
        data_response = self.send_request('post', self.authentication, data=data)
        BaseAPI.headers['Authorization'] = f'Bearer {data_response["access_token"]}'
        return data_response

    def get_initialization_status(self) -> str:
        """
        Pobranie statusu inicjacji Admina
        :return:
        """
        return self.send_request('get', self.init_done)['status']

    def patch_admin_password(self):
        """
        Sets password for Admin account
        :return:
        """
        data = json.dumps({'password': "Smartspaces1!"})
        self.send_request('patch', self.authentication, data=data)

    def get_version(self) -> dict:
        return self.send_request('get', self.version)
