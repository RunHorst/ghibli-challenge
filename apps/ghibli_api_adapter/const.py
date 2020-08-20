"""
URL definitions for the unofficial Ghibli Movie API
(https://ghibliapi.herokuapp.com/)
"""

GHIBLI_API_BASE_URL = 'https://ghibliapi.herokuapp.com'
GHIBLI_API_MOVIE_URL = f'{GHIBLI_API_BASE_URL}/films?limit=250'
GHIBLI_API_PEOPLE_URL = f'{GHIBLI_API_BASE_URL}/people?limit=250'

GHIBLI_MOVIES_CACHE_KEY = 'ghibli_movies'
GHIBLI_PEOPLE_CACHE_KEY = 'ghibli_people'
