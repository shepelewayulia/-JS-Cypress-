
import requests
import pytest


HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 3752})
    assert response.status_code == 200
    assert response.json()['id'] == '3752'

