import pytest

from apps.ghibli_api_adapter.const import (
    GHIBLI_API_MOVIE_URL,
    GHIBLI_API_PEOPLE_URL
)


@pytest.fixture
def ghibli_api_healthy_movies_response():
    '''
    A heavily abridged example of a Ghibli API /films endpoint response
    (with many irrelevant fields removed)

    (It would be nice to store this in a separate JSON file, but for a
    coding challenge it'll do)
    '''
    return [
        {
            'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe',
            'title': 'Castle in the Sky',
            'description': (
                'The orphan Sheeta inherited a mysterious crystal that links '
                'her to the mythical sky-kingdom of Laputa. With the help of '
                'resourceful Pazu and a rollicking band of sky pirates, she '
                'makes her way to the ruins of the once-great civilization. '
                'Sheeta and Pazu must outwit the evil Muska, who plans to use '
                'Laputa\'s science to make himself ruler of the world.'
            ),
            'people': [
                'https://ghibliapi.herokuapp.com/people/'
            ],
            'url': (
                'https://ghibliapi.herokuapp.com/films/'
                '2baf70d1-42bb-4437-b551-e5fed5a87abe'
            )
        },
        {
            'id': '12cfb892-aac0-4c5b-94af-521852e46d6a',
            'title': 'Grave of the Fireflies',
            'description': (
                'In the latter part of World War II, a boy and his sister, '
                'orphaned when their mother is killed in the firebombing of '
                'Tokyo, are left to survive on their own in what remains of '
                'civilian life in Japan. The plot follows this boy and his '
                'sister as they do their best to survive in the Japanese '
                'countryside, battling hunger, prejudice, and pride in their '
                'own quiet, personal battle.'
            ),
            'people': [
                'https://ghibliapi.herokuapp.com/people/'
            ],
            'species': [
                (
                    'https://ghibliapi.herokuapp.com/species/'
                    'af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
                )
            ],
            'url': (
                'https://ghibliapi.herokuapp.com/films/'
                '12cfb892-aac0-4c5b-94af-521852e46d6a'
            )
        },
        {
            'id': '58611129-2dbc-4a81-a72f-77ddfc1b1b49',
            'title': 'My Neighbor Totoro',
            'description': (
                'Two sisters move to the country with their father in order '
                'to be closer to their hospitalized mother, and discover the '
                'surrounding trees are inhabited by Totoros, magical spirits '
                'of the forest. When the youngest runs away from home, the '
                'older sister seeks help from the spirits to find her.'
            ),
            'people': [
            ],
            'url': (
                'https://ghibliapi.herokuapp.com/films/'
                '58611129-2dbc-4a81-a72f-77ddfc1b1b49'
            )
        }
    ]


@pytest.fixture
def ghibli_api_healthy_people_response():
    '''
    A heavily abridged example of a Ghibli API /people endpoint response
    (with some irrelevant fields removed). This payload explicitly doesn't
    cover all movies returned in `ghibli_api_healthy_movies_response` to make
    sure the code that builds relationships can deal with incomplete data

    (It would be nice to store this in a separate JSON file, but for a
    coding challenge it'll do)
    '''
    return [
        {
            'id': '986faac6-67e3-4fb8-a9ee-bad077c2e7fe',
            'name': 'Satsuki Kusakabe',
            'films': [
              'https://ghibliapi.herokuapp.com/films/'
              '58611129-2dbc-4a81-a72f-77ddfc1b1b49'
            ],
            'species': 'https://ghibliapi.herokuapp.com/species/'
                       'af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
            'url': 'https://ghibliapi.herokuapp.com/people/'
                   '986faac6-67e3-4fb8-a9ee-bad077c2e7fe'
        },
        {
            'id': 'd5df3c04-f355-4038-833c-83bd3502b6b9',
            'name': 'Mei Kusakabe',
            'films': [
              'https://ghibliapi.herokuapp.com/films/'
              '58611129-2dbc-4a81-a72f-77ddfc1b1b49'
            ],
            'species': 'https://ghibliapi.herokuapp.com/species/'
                       'af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
            'url': 'https://ghibliapi.herokuapp.com/people/'
                   'd5df3c04-f355-4038-833c-83bd3502b6b9'
        },
        {
            'id': '40c005ce-3725-4f15-8409-3e1b1b14b583',
            'name': 'Colonel Muska',
            'films': [
              'https://ghibliapi.herokuapp.com/films/'
              '2baf70d1-42bb-4437-b551-e5fed5a87abe'
            ],
            'species': 'https://ghibliapi.herokuapp.com/species/'
                       'af3910a6-429f-4c74-9ad5-dfe1c4aa04f2',
            'url': 'https://ghibliapi.herokuapp.com/people/'
                   '40c005ce-3725-4f15-8409-3e1b1b14b583'
        },
    ]


@pytest.fixture(autouse=True)
def ghibli_api_healthy_endpoints(
        requests_mock,
        ghibli_api_healthy_movies_response,
        ghibli_api_healthy_people_response):
    requests_mock.get(
        GHIBLI_API_MOVIE_URL,
        json=ghibli_api_healthy_movies_response
    )
    requests_mock.get(
        GHIBLI_API_PEOPLE_URL,
        json=ghibli_api_healthy_people_response
    )
