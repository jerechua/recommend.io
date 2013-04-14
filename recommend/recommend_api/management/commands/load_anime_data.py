from django.core.management.base import BaseCommand

from xml.etree import ElementTree

from recommend_api import models as api_models


class Command(BaseCommand):
    help = '''Loads the data coming from readme anime data sources. The
    data comes from ScudLee's animelist.xml which comes from anidb.net'''

    def handle(self, *args, **options):
        anime_titles = ElementTree.parse(args[0]).getroot()

        for anime in anime_titles.findall('anime'):
            anime_data = {
                'anidb_id': anime.get('aid'),
            }

            (anime_model, created) = api_models.Anime.objects.get_or_create(**anime_data)

            for title in anime:
                title_data = {
                    'type': title.get('type'),
                    'title': title.text,
                    'locale': title.get('{http://www.w3.org/XML/1998/namespace}lang'),
                    'anime': anime_model,
                }

                api_models.AnimeTitle.objects.get_or_create(**title_data)
