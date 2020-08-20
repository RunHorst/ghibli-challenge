from django.core.cache import cache
from django.urls import reverse
import pytest

from apps.ghibli_api_adapter.const import (
    GHIBLI_API_MOVIE_URL,
    GHIBLI_API_PEOPLE_URL
)

pytestmark = pytest.mark.django_db


"""
Mostly functional/integration tests
"""


def test_movie_list_page(
        client, requests_mock
        ):
    """
    Tests assuming the Ghibli API works
    """

    url = reverse('movies-overview')
    resp = client.get(url)

    assert resp.status_code == 200
    assert 'Totoro' in resp.content.decode()  # The only thing that matters
    # (in reality, we should add much more complex tests here regarding
    # the page content, although those test should probably be set up
    # via Selenium or something similar)

    """
    Tests assuming the Ghibli API doesn't work
    """

    # Remove any cached entries (to make sure the code actually
    # tries to get data from the mocked "Ghibli API")
    cache.clear()

    for endpoint in [GHIBLI_API_MOVIE_URL, GHIBLI_API_PEOPLE_URL]:
        requests_mock.get(
            endpoint,
            status_code=500
        )

        url = reverse('movies-overview')
        resp = client.get(url)

        assert resp.status_code == 200
        assert 'We\'re sorry' in resp.content.decode()  # See above caveat


def test_404(client):
    url = f'{reverse("movies-overview")}help-i-am-lost/'
    resp = client.get(url, status='*')

    assert resp.status_code == 404
    assert 'Looks like you\'re lost' in resp.content.decode()
