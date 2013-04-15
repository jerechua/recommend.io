from django.conf.urls import patterns, include, url

from rest_framework import generics

from recommend_anime import models as anime_models
from recommend_anime import serializers as anime_serializers

from recommend_api import views as api_views


defaults = {}
defaults['anime'] = {
    'serializer_class': anime_serializers.AnimeSerializer,
    'model': anime_models.Anime
}

urlpatterns = patterns('',
    url(r'anime/?$', generics.ListAPIView.as_view(**defaults['anime'])),
    url(r'autocomplete/(?P<anime_title>\w+)?$', api_views.AnimeAutoCompleteView.as_view()),
)
