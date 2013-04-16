from django.db.models import Count

from rest_framework import generics

from recommend_anime import models as anime_models
from recommend_anime import serializers as anime_serializers


class AnimeAutoCompleteView(generics.ListAPIView):

    def get_queryset(self):
        title = self.kwargs.get('anime_title')

        # Find all titles that match the title params, group by anime id
        titles_list = anime_models.Title.objects.values_list(
            'anime', flat=True).filter(title__contains=title).annotate(Count('anime'))

        # match the anime ids to the db
        animes = anime_models.Anime.objects.filter(anidb_id__in=set(titles_list))

        return animes
