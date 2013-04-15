from rest_framework import serializers

from recommend_anime import models as anime_models

class AnimeSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = anime_models.Anime
        fields = ('anidb_id', 'title')

    title = serializers.CharField(source='title')


