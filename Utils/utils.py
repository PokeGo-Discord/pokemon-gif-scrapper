"""
pokemon-gif-scrapper
Scrap gif of all pokemon of each generation with Beautifulsoup webscrapping

FILE: utils.py
"""

import requests
from bs4 import BeautifulSoup

# Retrieve All Pokemon Names By Generation Id
def getPokemonNames(gen_id):
    url = "https://pokeapi.co/api/v2/generation/" + str(gen_id) + "/"
    r = requests.get(url)
    data = r.json()
    pokemonNames=[]
    for i in data['pokemon_species']:
        pokemonNames.append(i['name'])
    return pokemonNames



