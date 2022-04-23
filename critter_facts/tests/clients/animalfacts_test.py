import pytest
import json
import requests_mock
from datetime import datetime
from critter_facts.clients.animalfacts import AnimalFacts

@pytest.fixture()
def fake_cat_facts():
    with open("critter_facts/tests/fixtures/cat_facts.json") as f:
        return json.load(f)

@pytest.fixture()
def fake_dog_facts():
    with open("critter_facts/tests/fixtures/dog_facts.json") as f:
        return json.load(f)

def test_init():
    animal_facts = AnimalFacts()
    assert animal_facts.animal_facts_url == "http://animalfacts.org/api/v0"
    assert animal_facts.fetch_accesstoken_url == "http://animalfacts.org/api/v0/fetch_token"
    assert animal_facts.refresh_accesstoken_url == "http://animalfacts.org/api/v0/refresh_token"
    assert animal_facts.client_id == "test123"
    assert animal_facts.client_secret == "top_secret"
    assert animal_facts.timeout == 5

def test_fetch_facts_cat(fake_cat_facts):
    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/cat/facts/", json=fake_cat_facts)

        animal_facts = AnimalFacts()
        setattr(animal_facts, "accesstoken", {
            'token': 'abc123',
            'refresh_token': 'abc123',
            'granted_at': datetime.now(),
            'expiration': 3600
        }) 
        cat_facts = animal_facts.fetch_facts("cat")

        assert len(cat_facts) == 5
        assert cat_facts[-1]['animal'] == "cat"        
        assert cat_facts[-1]['fact'] == "they choose you, not the other way around." 
        last_request = rm.request_history[0]      
        assert "Bearer abc123" == last_request.headers.get("Authorizaton")

def test_fetch_facts_dog(fake_dog_facts):
    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/dog/facts/", json=fake_dog_facts)

        animal_facts = AnimalFacts()
        setattr(animal_facts, "accesstoken", {
            'token': 'abc123',
            'refresh_token': 'abc123',
            'granted_at': datetime.now(),
            'expiration': 3600
        })
        dog_facts = animal_facts.fetch_facts("dog")

        assert len(dog_facts) == 5
        assert dog_facts[-1]['animal'] == "dog"        
        assert dog_facts[-1]['fact'] == "some like to go for a walk."
        last_request = rm.request_history[0]      
        assert "Bearer abc123" == last_request.headers.get("Authorizaton")

def test_fetch_facts_accesstoken_memoization(fake_cat_facts, fake_dog_facts):
    animal_facts = AnimalFacts()
    setattr(animal_facts, "accesstoken", {
        'token': 'abc123',
        'refresh_token': 'abc123',
        'granted_at': datetime.now(),
        'expiration': 3600
    })

    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/cat/facts/", json=fake_cat_facts)

        cat_facts = animal_facts.fetch_facts("cat")
        assert len(cat_facts) == 5
        last_request = rm.request_history[-1]      
        assert "Bearer abc123" == last_request.headers.get("Authorizaton")

    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/dog/facts/", json=fake_dog_facts)

        dog_facts = animal_facts.fetch_facts("dog")
        assert len(dog_facts) == 5
        last_request = rm.request_history[-1]      
        assert "Bearer abc123" == last_request.headers.get("Authorizaton")
