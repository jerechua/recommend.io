from django.db.models import Count

from rest_framework import generics

from recommend_anime import models as anime_models
from recommend_anime import serializers as anime_serializers

class AnimeAutoCompleteView(generics.ListAPIView):

    serializer_class = anime_serializers.TitleToAnimeSerializer

    def get_queryset(self):
        title = self.kwargs.get('anime_title')

        titles = anime_models.Title.objects.filter(title__contains=title).filter(type='main')

        return titles