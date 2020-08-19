from django.shortcuts import render

from apps.ghibli_api_adapter.exceptions import GhibliAPIException
from apps.ghibli_api_adapter.lib import retrieve_movie_list


def movies_overview(request):
    try:
        movie_list = retrieve_movie_list()
    except GhibliAPIException:
        return render(
            request,
            'movie-list/api_issue.html'
        )

    return render(
        request,
        'movie-list/index.html',
        {
            'movies': movie_list
        }
    )


def catch_404(request, exception):
    return render(
        request,
        'errors/404.html',
        status=404
    )
