from flask import Flask
import animalfacts

app = Flask(__name__)

@app.route('/cat_facts')
def cat_facts():
    cat_facts = animalfacts.Client.fetch_facts('cat')
    return cat_facts

@app.route('/dog_facts')
def dog_facts():
    dog_facts = animalfacts.Client.fetch_facts('dog')
    return dog_facts