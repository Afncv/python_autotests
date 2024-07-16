import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = 'd35d067c55d03851a5569b49742003a5'
Header = {'Content-Type' : 'application/json', 'trainer_token' : token}

body_create = {    "name": "Зевс",
    "photo_id": 2
}

body_change = {
    "pokemon_id": "43878",
    "name": "Кураж",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "43878"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = Header, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = Header, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = body_pokeball)
print(response_pokeball.text)
