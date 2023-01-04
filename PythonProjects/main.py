import requests
import json

token = 'd6815ba29c757fb07093b857918f01ee'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Charmander",
    "photo": "https://dolnikov.ru/pokemons/05.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 2848,
    "name": "Charmander666",
    "photo": "https://dolnikov.ru/pokemons/05.png"
})

print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token' : token}, json={
  "pokemon_id": "2848"  
})

print(response_post.text)
