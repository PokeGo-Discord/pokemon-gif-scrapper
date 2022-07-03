"""
pokemon-gif-scrapper
Scrap gif of all pokemon of each generation with Beautifulsoup webscrapping

FILE: scrapper.py
"""

import Utils.utils as utils

pokemonName = utils.getPokemonNames(1)
exeptional = []

for p in pokemonName:
    url = utils.getPokemonGifUrl(p)
    if utils.testUrl(url):
        urlShiny = utils.getPokemonShinyGifUrl(p)
        name = p + ".gif"
        utils.saveGif('./Result/Gen-1/Normal/' + name, url)
        utils.saveGif('./Result/Gen-1/Shiny/'  + name, urlShiny)
        print('Succesfully save: ' + p)
    else:
        exeptional.append(p)
        print("Can't save: " + p)


    
