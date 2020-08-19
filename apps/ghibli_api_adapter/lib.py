import json
import requests

from .const import (
    GHIBLI_API_MOVIE_URL,
    GHIBLI_API_PEOPLE_URL
)
from .exceptions import GhibliAPIException


def _fetch_movies():
    resp = requests.get(GHIBLI_API_MOVIE_URL)

    try:
        return resp.json()
    except json.decoder.JSONDecodeError:
        raise GhibliAPIException


def _fetch_characters():
    resp = requests.get(GHIBLI_API_PEOPLE_URL)

    try:
        return resp.json()
    except json.decoder.JSONDecodeError:
        raise GhibliAPIException


def retrieve_movie_list():
    movies = _fetch_movies()
    characters = _fetch_characters()

    if not len(movies):
        raise GhibliAPIException

    return [
        movie['title']
        for movie in movies
    ]
