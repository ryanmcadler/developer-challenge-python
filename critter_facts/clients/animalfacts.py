import requests

http_client = requests.Session()

class AnimalFacts:
    def __init__(self):
        self.animal_facts_url = "http://animalfacts.org/api/v0"
        self.fetch_accesstoken_url = "{}/fetch_token".format(self.animal_facts_url)
        self.refresh_accesstoken_url = "{}/refresh_token".format(self.animal_facts_url)
        self.client_id = "test123"
        self.client_secret = "top_secret"
        self.timeout = 5
        self.accesstoken = {}
    
    def fetch_facts(self, animal):
        url = "{}/animals/{}/facts/".format(self.animal_facts_url, animal)
        resp = http_client.get(url, timeout=self.timeout)
        return resp.json()