from django.core.management.base import BaseCommand

from xml.etree import ElementTree

from recommend_api import models as api_models


class Command(BaseCommand):
    help = '''Loads the data coming from readme anime data sources. The
    data comes from ScudLee's animelist.xml which comes from anidb.net'''

    def handle(self, *args, **options):
        anime_titles = ElementTree.parse(args[0]).getroot()

        bulk_anime = []
        bulk_titles = []

        for anime in anime_titles.findall('anime'):
            anime_data = {
                'anidb_id': anime.get('aid'),
            }

            anime_model = api_models.Anime.objects.filter(**anime_data)
            if anime_model.exists():
                anime_model = anime_model[0]
            else:
                anime_model = api_models.Anime(**anime_data)
                bulk_anime.append(anime_model)

            for title in anime:
                title_data = {
                    'type': title.get('type'),
                    'title': title.text,
                    'locale': title.get('{http://www.w3.org/XML/1998/namespace}lang'),
                    'anime': anime_model,
                }

                title_model = api_models.AnimeTitle.objects.filter(**title_data)
                if not title_model.exists():
                    bulk_titles.append(api_models.AnimeTitle(**title_data))

        api_models.Anime.objects.bulk_create(bulk_anime)
        api_models.AnimeTitle.objects.bulk_create(bulk_titles)