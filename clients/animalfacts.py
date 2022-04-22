import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

http_client = requests.session()
http_client.verify = True
retry = Retry(
    total=3,
    backoff_factor=0.9,
    status_forcelist=[501, 502, 503, 504],
    method_whitelist={"GET", "POST"},
)
http_client.mount("https://", HTTPAdapter(max_retries=retry))

class Client:
    def __init__(self, animal_facts_url):
        self.animal_facts_url = animal_facts_url

    def fetch_facts(self, animal):
        url = "{}/v0/animal/{}/facts/".format(
            self.animal_facts_url, animal
        )
        resp = http_client.get(url, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()