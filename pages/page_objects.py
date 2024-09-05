import requests

class ApiPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, json=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=json, data=data)
        return response

    def put(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=json)
        return response

    def delete(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, params=params)
        return response
