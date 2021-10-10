import json

import requests


class BaseAPI:
    def __init__(self):
        self.base_url = 'http://192.168.1.254/api/'
        self.authentication = 'authentication'

    def send_request(self, request_type: str, url: str, **kwargs) -> dict:
        """
        Wysłanie żądania do aplikacji po stronie API
        :param request_type: typ żądania, tj. 'post', 'put', 'get' albo 'delete'
        :param url: ścieżka żądania, która będzie dodana do podstawowej ścieżki
        :return: Słownik z wartością zwróconą
        """
        call = getattr(requests, request_type)
        return call(self.base_url + url, **kwargs).json()

    def authorize(self):
        data = {
            "login": "Admin",
            "password": "Smartspaces1!",
            "tool": "Configuration"
        }
        data = json.dumps(data)
        self.send_request('post', self.authentication, data=data)
