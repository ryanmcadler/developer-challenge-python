from flask import Flask
from critter_facts.clients.animalfacts import AnimalFacts

app = Flask(__name__)

@app.route('/cat_facts')
def cat_facts():
    cat_facts = AnimalFacts.fetch_facts('cat')
    return cat_facts

@app.route('/dog_facts')
def dog_facts():
    dog_facts = AnimalFacts.fetch_facts('dog')
    return dog_facts