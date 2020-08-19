from django.shortcuts import render

from apps.ghibli_api_adapter.lib import retrieve_movie_list


def movies_overview(request):
    movie_list = retrieve_movie_list()

    return render(
        request,
        'movie-list/index.html',
        {
            'movies': movie_list
        }
    )
