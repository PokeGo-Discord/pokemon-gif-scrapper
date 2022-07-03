"""
pokemon-gif-scrapper
Scrap gif of all pokemon of each generation with Beautifulsoup webscrapping

FILE: utils.py
"""

import requests
import urllib.request
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

def getPokemonGifUrl(pokemonName):
    url = "https://projectpokemon.org/images/normal-sprite/" + pokemonName + ".gif"
    return url

def getPokemonShinyGifUrl(pokemonName):
    url = "https://projectpokemon.org/images/shiny-sprite/" + pokemonName + ".gif"
    return url

def testUrl(url):
    page = requests.get(url)
    if(page.status_code==200):
        return True
    else:
        return False
    
def countAllPokemonFromPokeApi():
    id = 1
    counter = 0
    for i in range(8):
        url = "https://pokeapi.co/api/v2/generation/" + str(id) + "/"
        r = requests.get(url)
        data = r.json()
        counter = counter + len(data['pokemon_species'])
    return counter

def countAllPokemonFromPokeApiByGen(gen_id):
    counter = 0
    url = "https://pokeapi.co/api/v2/generation/" + str(gen_id) + "/"
    r = requests.get(url)
    data = r.json()
    counter = len(data['pokemon_species'])
    return counter

def saveGif(folderPath, url):
    urllib.request.urlretrieve(url, folderPath)

    


