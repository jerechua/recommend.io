from django.db import models

from django.contrib.auth.models import User as django_auth_user


class Anime(models.Model):
    anidb_id = models.IntegerField(primary_key=True, null=False, unique=True)

    @property
    def title(self):
        return self.animetitle_set.get(type='main').title

    def __str__(self):
        return "%s - %s" % (self.anidb_id, self.title)


class AnimeTitle(models.Model):
    anime = models.ForeignKey('Anime', null=False)
    locale = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=20)

    def __str__(self):
        return "%s - %s (%s)" % (self.type, self.title, self.locale)


class BaseModel(models.Model):
    modify_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class AnimeRating(BaseModel):
    user = models.ForeignKey('User', null=False)
    anime = models.ForeignKey('Anime', null=False)
    rating = models.PositiveIntegerField()


class UserProfile(django_auth_user):
    picture = models.CharField(max_length=150)

    def get_anime_rating(anime):
        """
        """

        return AnimeRating.objects.filter(user=self, anime=anime).rating
