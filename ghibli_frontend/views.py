from django.http import HttpResponse

from ghibli_api_adapter.lib import retrieve_movie_list


def movies_overview(request):
    movie_list = [
        f'<li>{movie}</li>'
        for movie in retrieve_movie_list()
    ]

    return HttpResponse(
        f'<h3>Ghibli movies:</h3>'
        f'<ul>{"".join(movie_list)}</ul>'
        f'<p>Hier könnte Ihre Werbung stehen.</p>'
    )
