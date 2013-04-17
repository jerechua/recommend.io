from django.db import models

from third_party.tvdb import Tvdb

from recommend_core import models as core_models

class Anime(models.Model):
    anidb_id = models.IntegerField(primary_key=True, null=False, unique=True)
    tvdb_id = models.IntegerField(null=True, blank=True) 
    imdb_id = models.CharField(max_length=30, null=True, blank=True)
    # only grab these fields when we need it to conserve space
    # and less api calls
    description = models.CharField(max_length=255, null=True, blank=True)
    network = models.CharField(max_length=50, null=True, blank=True)
    first_aired = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre')
    banner_url = models.URLField(max_length=100, null=True, blank=True)
    poster_url = models.URLField(max_length=100, null=True, blank=True)
    fanart_url = models.URLField(max_length=100, null=True, blank=True)


    @property
    def title(self):
        return self.title_set.get(type='main').title

    @property
    def title_en(self):
        title = self.title_set.filter(locale='en')
        if title.exists():
            return title[0].title

    def verify_data(self, *args, **kwargs):
        """
        grabs tvdb data
        """

        if self.description is None:
            data = Tvdb().get_series_by_id(self.tvdb_id)
            self.description = data['description']
            self.network = data['network']
            self.first_aired = data['first_aired']
            for genre in data['genre']:
                (genre_model, created) = Genre.objects.get_or_create(genre=genre)
                self.genre.add(genre_model)
            self.banner_url = data['banner_url']
            self.poster_url = data['poster_url']
            self.fanart_url = data['fanart_url']
            self.save()

        return self



    def __str__(self):
        return "%s - %s" % (self.anidb_id, self.title)

class Genre(models.Model):
    genre = models.CharField(max_length=50, null=False, blank=False, unique=True)


class Title(models.Model):
    anime = models.ForeignKey('Anime', null=False)
    locale = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=20)

    def __str__(self):
        return "%s - %s (%s)" % (self.type, self.title, self.locale)


class Rating(core_models.BaseModel):
    user = models.ForeignKey('recommend_api.UserProfile', null=False)
    anime = models.ForeignKey('Anime', null=False)
    rating = models.PositiveIntegerField()