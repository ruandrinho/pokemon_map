import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import PokemonEntity, Pokemon
from django.utils.timezone import localtime, now


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    time_now = localtime(now())
    pokemon_entities_for_map = PokemonEntity.objects.filter(appeared_at__lte=time_now, disappeared_at__gte=time_now)
    for entity in pokemon_entities_for_map:
        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            request.build_absolute_uri(entity.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_for_list = []
    for pokemon in pokemons:
        pokemons_for_list.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_for_list,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    time_now = localtime(now())
    pokemon = Pokemon.objects.get(id=pokemon_id)
    for entity in pokemon.entities.filter(appeared_at__lte=time_now, disappeared_at__gte=time_now):
        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            request.build_absolute_uri(pokemon.image.url)
        )

    pokemon_data_for_page = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description
    }
    if pokemon.evoluted_from is not None:
        pokemon_data_for_page['previous_evolution'] = {
            'pokemon_id': pokemon.evoluted_from.id,
            'img_url': request.build_absolute_uri(pokemon.evoluted_from.image.url),
            'title_ru': pokemon.evoluted_from.title
        }
    if pokemon.evoluted_to.count() > 0:
        pokemon.evoluted_to_first = pokemon.evoluted_to.first()
        pokemon_data_for_page['next_evolution'] = {
            'pokemon_id': pokemon.evoluted_to_first.id,
            'img_url': request.build_absolute_uri(pokemon.evoluted_to_first.image.url),
            'title_ru': pokemon.evoluted_to_first.title
        }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data_for_page
    })
