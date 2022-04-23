import pytest
import json
import requests
import requests_mock
from critter_facts.clients.animalfacts import AnimalFacts

@pytest.fixture()
def fake_cat_facts():
    with open("critter_facts/tests/fixtures/cat_facts.json") as f:
        return json.load(f)

@pytest.fixture()
def fake_dog_facts():
    with open("critter_facts/tests/fixtures/dog_facts.json") as f:
        return json.load(f)

def test_fetch_facts_cat(fake_cat_facts):
    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/cat/facts/", json=fake_cat_facts)

        animal_facts = AnimalFacts()
        cat_facts = animal_facts.fetch_facts('cat')
        assert len(cat_facts) == 5

def test_fetch_facts_dog(fake_dog_facts):
    with requests_mock.Mocker() as rm:
        rm.get("http://animalfacts.org/api/v0/animals/dog/facts/", json=fake_dog_facts)

        animal_facts = AnimalFacts()
        dog_facts = animal_facts.fetch_facts('dog')
        assert len(dog_facts) == 5