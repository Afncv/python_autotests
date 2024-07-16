import requests
import pytest 


URL = 'https://api.pokemonbattle.ru/v2'
token = 'd35d067c55d03851a5569b49742003a5'
Header = {'Content-Type' : 'application/json', 'trainer_token' : token}
TRAINER_ID = '4382'

def tests_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def tests_trainers_name():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["trainer_name"] == 'Чарм'

        