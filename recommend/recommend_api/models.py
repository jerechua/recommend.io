from django.db import models

from django.contrib.auth.models import User as django_auth_user

from recommend_anime import models as anime_models


class UserProfile(django_auth_user):
    picture = models.CharField(max_length=150)

    def get_anime_rating(anime):
        """
        """

        return anime_models.AnimeRating.objects.filter(user=self, anime=anime).rating
