from django.core.cache import cache
import json
import requests

from .const import (
    GHIBLI_API_MOVIE_URL,
    GHIBLI_API_PEOPLE_URL,
    GHIBLI_MOVIES_CACHE_KEY,
    GHIBLI_PEOPLE_CACHE_KEY
)
from .exceptions import GhibliAPIException


def _fetch_movies(force_refresh_cache=False):
    movies = cache.get(GHIBLI_MOVIES_CACHE_KEY)
    if force_refresh_cache or not movies:
        resp = requests.get(GHIBLI_API_MOVIE_URL)

        try:
            movies = resp.json()
            cache.set(GHIBLI_MOVIES_CACHE_KEY, movies, timeout=60)
        except (json.decoder.JSONDecodeError):
            raise GhibliAPIException
    return movies


def _fetch_characters(force_refresh_cache=False):
    characters = cache.get(GHIBLI_PEOPLE_CACHE_KEY)
    if force_refresh_cache or not characters:
        resp = requests.get(GHIBLI_API_PEOPLE_URL)

        try:
            characters = resp.json()
            cache.set(GHIBLI_PEOPLE_CACHE_KEY, characters, timeout=60)
        except (json.decoder.JSONDecodeError):
            raise GhibliAPIException
    return characters


def retrieve_movie_list():
    movies = _fetch_movies()

    # Init character list for each movie
    for movie in movies:
        movie['characters'] = []

    # The characters actually reference "their" movie
    # by URL, so the URL should be the "primary key"
    movies = {movie['url']: movie for movie in movies}

    characters = _fetch_characters()

    for character in characters:
        try:
            for related_movie in character['films']:
                movies[related_movie]['characters'].append(character)
        except KeyError:
            # We *could* separately display any with faulty
            # movie relationship - but let's not, for now
            pass

    if not len(movies):
        raise GhibliAPIException

    # We could strip out most of the movie/character
    # fields at this point (age, gender etc.), but let's leave them in
    # and leave the (theoretical) template designers as much freedom as they want

    return movies.values()
