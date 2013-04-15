from django.db import models

from recommend_core import models as core_models

class Anime(models.Model):
    anidb_id = models.IntegerField(primary_key=True, null=False, unique=True)

    # @property
    def title(self):
        return self.titles_set.get(type='main').title

    def __str__(self):
        return "%s - %s" % (self.anidb_id, self.title)


class Titles(models.Model):
    anime = models.ForeignKey('Anime', null=False)
    locale = models.CharField(max_length=10)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=20)

    def __str__(self):
        return "%s - %s (%s)" % (self.type, self.title, self.locale)


class Ratings(core_models.BaseModel):
    user = models.ForeignKey('recommend_api.UserProfile', null=False)
    anime = models.ForeignKey('Anime', null=False)
    rating = models.PositiveIntegerField()