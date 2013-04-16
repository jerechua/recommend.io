from rest_framework import serializers

from recommend_anime import models as anime_models


class AnimeSerializer(serializers.ModelSerializer):

    """
    Serializes the anime data for rest_framework
    """

    class Meta:
        model = anime_models.Anime
        fields = ('id', 'title')

    id = serializers.IntegerField(source='anidb_id')
    title = serializers.CharField(source='title')


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = anime_models.Title
        fields = ('locale', 'title', 'type')

