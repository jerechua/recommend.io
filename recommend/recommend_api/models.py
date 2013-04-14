from django.db import models


class Anime(models.Model):
    anidb_id = models.IntegerField(primary_key=True, null=False, unique=True)


class AnimeTitle(models.Model):
    anime = models.ForeignKey('Anime', null=False)
    locale = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=20)
