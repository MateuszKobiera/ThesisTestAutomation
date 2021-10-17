import json

import requests


class BaseAPI:
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json'}

    def __init__(self):
        self.base_url = 'http://192.168.1.254/api/'
        self.authentication = 'authentication'
        self.authorize()

    def send_request(self, request_type: str, url: str, **kwargs) -> dict:
        """
        Wysłanie żądania do aplikacji po stronie API
        :param request_type: typ żądania, tj. 'post', 'put', 'get' albo 'delete'
        :param url: ścieżka żądania, która będzie dodana do podstawowej ścieżki
        :return: Słownik z wartością zwróconą
        """
        call = getattr(requests, request_type)
        response = call(self.base_url + url, headers=BaseAPI.headers, **kwargs).json()
        # if url != 'authentication' and :
        #     if response['status'] not in [200, 201, 202] and type(response['status']) == int:
        #         raise TypeError(response)
        return response

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
