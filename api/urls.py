#!
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import pokemon_list, get_pokemon, pokemon_list_type

urlpatterns = [
    url(r'^$', pokemon_list, name="pokemon_list"),
    url(r'^pokemon-list/$', pokemon_list, name="pokemon_list"),
    url(r'^pokemon/(?P<pokemon_id>[\d{1,7}]+)/$', get_pokemon, name="get_pokemon"),
    url(r'^pokemon-list/(?P<pokemon_type>[-\w]+)/$', pokemon_list_type, name="pokemon_list_type"),
]