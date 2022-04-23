# developer-challenge-python
A simple Flask-based exercise to pair on with interview candidates.

## Installation
Install Python 3.9.12 and setup a virtualenv for the application.  Set `PYTHONPATH` to reference source directory.  Install requirements using pip:
```
pip install --no-cache-dir --ignore-installed -r requirements.txt
```

## The Challenge
Hypthetical Scenario: The company uses this app as a proxy to retreive dog and cat facts from a fictional API (animalfacts.org).  Due to the API increasing in popularity, they implemented OAuth authentication; client applications now have to authenticate using a client credentials flow in order to fetch animal facts.
How do we update the `critter_facts.clients.animalfacts` module so that we implement OAuth authentication when we call the animal facts endpoint?  Given that we're billed on number of access tokens generated, how do we implement authentication so that we're not requesting an access token on each request and we minimize the number of access tokens that we fetch?  There is a simple test suite including with this project that provides some simple specs that test the presence of the access token in requests made to animalfacts.org and there is a spec that is intended to ensure that we're not overeagerly fetching access tokens; upon successful completion of this exercise, those tests should pass.

You can run these test by running:
```
pytest critter_facts/tests/clients/animalfacts_test.py
```

Assume that we can use the token fetch endpoints defined in `critter_facts.clients.animalsfacts` to fetch tokens and refresh tokens and that these endpoints return a JSON object with `token`, `refresh_token`, `granted_at` (datetime), and `expiration` (seconds) attributes.

###### Bonus Challenge
How do we ensure that we refresh an access token when it expires?  Can we write a spec to test this behavior?