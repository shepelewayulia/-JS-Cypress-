import requests


responce = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                         json={
                            "name": "Каравайка",
                            "photo": "https://dolnikov.ru/pokemons/albums/004.png"
                         },
                         headers={"trainer_token": "1e5bf37f2cd9ce1d20adbe1d8ca727f1",
                                  'Content-Type':'application/json'}
                         
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')



responce = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                         json={
                            "pokemon_id": 20444,
                            "name": "Дракула",
                            "photo": "https://dolnikov.ru/pokemons/albums/007.png"
                        
                         },
                         headers={"trainer_token": "099e375fbd583f7b82fb79f0df6c56f7",
                                  'Content-Type':'application/json'}
                         
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')


responce = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         json={
                            "pokemon_id": "20444"
                         },
                         headers={"trainer_token": "099e375fbd583f7b82fb79f0df6c56f7",
                                  'Content-Type':'application/json'}
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')