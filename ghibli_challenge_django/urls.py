from django.contrib import admin
from django.urls import path

from apps.ghibli_frontend.views import movies_overview

urlpatterns = [
    path('', movies_overview, name='movies-overview'),
]
