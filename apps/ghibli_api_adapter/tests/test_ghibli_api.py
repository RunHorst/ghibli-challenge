import pytest

from apps.ghibli_api_adapter.const import (
    GHIBLI_API_MOVIE_URL,
    GHIBLI_API_PEOPLE_URL
)
from apps.ghibli_api_adapter.exceptions import GhibliAPIException
from apps.ghibli_api_adapter.lib import (
    _fetch_movies,
    retrieve_movie_list
)

"""
Unit(ish) tests
"""


def test_fetching_the_movie_list(
        requests_mock,
        ghibli_api_healthy_movies_response
        ):
    """
    Normal functionality when everything's fine
    """
    movies = retrieve_movie_list()
    assert len(movies) == len(ghibli_api_healthy_movies_response)

    """
    Ghibli API is down
    """
    for endpoint in [GHIBLI_API_MOVIE_URL, GHIBLI_API_PEOPLE_URL]:
        with pytest.raises(GhibliAPIException):
            requests_mock.get(endpoint, status_code=500)
            _fetch_movies()


def test_preprocessing_the_movie_list(
        requests_mock,
        ghibli_api_healthy_movies_response
        ):
    movie_list = retrieve_movie_list()
    assert len(movie_list) == len(ghibli_api_healthy_movies_response)
