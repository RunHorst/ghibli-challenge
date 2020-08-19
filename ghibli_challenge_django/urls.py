from django.contrib import admin
from django.urls import path

from apps.ghibli_frontend.views import (
    catch_404,
    movies_overview
)

urlpatterns = [
    path('', movies_overview, name='movies-overview'),
]

handler404 = catch_404
