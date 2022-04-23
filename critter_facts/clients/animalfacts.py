import requests

http_client = requests.Session()
accesstoken = {}

class AnimalFacts:
    def __init__(self):
        # initialize client
        #self.fetch_accesstoken()
        self.animal_facts_url = "http://animalfacts.org/api/v0"
        self.fetch_accesstoken_url = "{}/fetch_token".format(self.animal_facts_url)
        self.refresh_accesstoken_url = "{}/refresh_token".format(self.animal_facts_url)
        self.client_id = "test123"
        self.client_secret = "top_secret"
        self.timeout = 5
    
    def fetch_facts(self, animal):
        url = "{}/animals/{}/facts/".format(self.animal_facts_url, animal)
        resp = http_client.get(url, timeout=self.timeout)
        return resp.json()
    
    def fetch_accesstoken(self):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        resp = http_client.post(self.fetch_accesstoken_url, timeout=self.timeout, data=params)

        accesstoken['token'] = resp['token']
        accesstoken['refresh_token'] = resp['refresh_token']
        accesstoken['expiration'] = resp['expiration']

        http_client.headers.update({'Authorization': "Bearer {}".format(accesstoken['token'])})