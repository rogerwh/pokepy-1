#!
# -*- coding: utf-8 -*-

from django.shortcuts import render

import requests
import json


def pokemon_list(request):

    endpoint = "https://pokeapi.co/api/v2/pokemon/?limit=30"
    response = create_request(endpoint)

    titulo = "Lista de Pokemon"

    response_pokemon = response.get("results", None)
    pokemon_list = []

    for pokemon in response_pokemon:
        response = create_request(pokemon.get("url"))
        name_pokemon = response.get("name", "Unknown")
        imagen_pokemon = response.get("sprites").get("front_default")
        pokemon_id = response.get("id")
        
        pokemon_list.append({
            'name': name_pokemon.capitalize(), 
            'image': imagen_pokemon, 
            "id": pokemon_id})

    return render(request, 'lista_pokemon.html', {"pokemon_list": pokemon_list, "titulo": titulo})


def pokemon_list_type(request, pokemon_type):
    
    endpoint = "https://pokeapi.co/api/v2/type/{}/".format(pokemon_type)
    response = create_request(endpoint)

    titulo = "Lista de Pokemon de tipo {}".format(pokemon_type)

    response_pokemon = response.get("pokemon", None)
    pokemon_list = []

    pokemon_limit = 30
    for dict_pokemon in response_pokemon:
        if pokemon_limit == 0:
            break
        endpoint_pokemon = dict_pokemon.get("pokemon").get("url")
        
        response = create_request(endpoint_pokemon)
        name_pokemon = response.get("name", "Unknown")
        imagen_pokemon = response.get("sprites").get("front_default")
        pokemon_id = response.get("id")
        
        pokemon_list.append({
            'name': name_pokemon.capitalize(), 
            'image': imagen_pokemon, 
            "id": pokemon_id})
        pokemon_limit = pokemon_limit - 1
    return render(request, 'lista_pokemon.html', {"pokemon_list": pokemon_list, 'titulo':titulo})

def get_pokemon(requests, pokemon_id):
    
    endpoint = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_id)
    response = create_request(endpoint)

    pokemon_id = response.get("id")
    name = response.get("name").capitalize()

    height = response.get("height") # Altura
    weight = response.get("weight") # Peso
    
    types_temp = response.get("types") # Lista
    types = []
    for _type in types_temp:
        _type = _type.get("type")
        types.append(_type)

    abilities_temp = response.get("abilities") # List
    abilities = []
    for ability in abilities_temp:
        ability = ability.get("ability")
        abilities.append(ability)
    
    moves_temp = response.get("moves") # List
    moves = []
    for move in moves_temp:
        move = move.get("move")
        moves.append(move)
    
    sprites = response.get("sprites")
    back_default = sprites.get("back_default")
    front_default = sprites.get("front_default")
    back_shiny = sprites.get("back_shiny")
    front_shiny = sprites.get("front_shiny")

    images_list = [
        back_default,
        front_default,
        back_shiny,
        front_shiny
    ]

    pokemon = {
        "id": pokemon_id,
        "name": name,
        "height": height,
        "weight": weight,
        "types": types,
        "abilities": abilities,
        "moves": moves,
        "sprites": images_list
    }

    return render(requests, 'pokemon.html', {'pokemon': pokemon})

def create_request(endpoint):
    
    try:
        response = requests.get(endpoint)
        response = json.loads(response.text)
    except Exception as e:
        response = {}

    return response