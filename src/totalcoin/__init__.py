# -*- coding: utf-8 -*-
try:
    from urlparse import urljoin
except ImportError:  # python 3
    from urllib.parse import urljoin

import requests
import json


BASE_API_URL = 'https://api.totalcoin.com/ar/'


class Api(object):
    """Clase para interactuar con el API de TotalCoin."""

    def __init__(self, client_email, api_key, api_url=None):
        self.__email = client_email
        self.__key = api_key
        self.__url = api_url or BASE_API_URL

    def __request(self, method, uri, params=None, headers=None):
        """Retorna un diccionario con el resultado de la consulta al API."""

        headers = headers if isinstance(headers, dict) else {}
        params = params if isinstance(params, dict) else {}
        request = getattr(requests, method)
        url = urljoin(self.url, uri)

        if method in ['get', 'delete']:
            response = request(url, headers=headers)
        if method in ['post', 'put']:
            headers.update({'content-type': 'application/json'})
            response = request(url, data=json.dumps(params), headers=headers)

        response.raise_for_status()

        return response.json()

    def __get_access_token(self):
        """Retorna el token del usuario."""

        uri = 'Security'
        params = {'Email': self.email, 'ApiKey': self.key}
        response = self.__request('post', uri, params)

        if response['IsOk']:
            return response['Response']['TokenId']

        return response

    @property
    def email(self):
        return self.__email

    @property
    def key(self):
        return self.__key

    @property
    def url(self):
        return self.__url

    @property
    def access_token(self):
        """Retorna el token del usuario."""

        return self.__get_access_token()

    def perform_checkout(self, params):
        """Retorna el resultado de la operacion de checkout como un dict."""

        uri = 'Checkout/{}'.format(self.access_token)
        response = self.__request('post', uri, params)
        if response['IsOk']:
            return response['Response']

        return response

    def get_merchants(self):
        """Retorna una lista de merchants."""
        uri = 'Merchant/{}'.format(self.access_token)
        response = self.__request('get', uri)
        if response['IsOk']:
            return response['Response']

        return response

    def get_ipn_info(self, reference_id, token=None):
        if token is None:
            token = self.access_token
        uri = 'Ipn/{}/{}'.format(token, reference_id)
        response = self.__request('get', uri)
        if response['IsOk']:
            return response['Response']

        return response
