import requests

class ApiPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        """Send a GET request to the specified endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response
