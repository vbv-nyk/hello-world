import requests

class Fetcher:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.data = response.json()
        return self.data
