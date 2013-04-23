from django.core.management.base import BaseCommand, CommandError

from xml.etree import ElementTree

from recommend_anime import models as anime_models


class Command(BaseCommand):
    help = '''Loads the data coming from readme anime data sources. The
    data comes from ScudLee's animetitles.xml which comes from anidb.net'''

    def handle(self, *args, **options):

        if len(args) == 0:
            raise CommandError('No directory supplied')

        base_path = args[0]

        animetitles_xml = '%s/animetitles.xml' % (base_path)
        animelistmaster_xml = '%s/anime-list-master.xml' % (base_path)

        try:
            with open(animetitles_xml): pass
        except IOError:
            raise CommandError('%s does not exist' % (animetitles_xml))

        try:
            with open(animelistmaster_xml): pass
        except IOError:
            raise CommandError('%s does not exist' % (animelistmaster_xml))


        # Load animetitles.xml first
        anime_titles = ElementTree.parse(animetitles_xml).getroot()
        anime_tvdb = ElementTree.parse(animelistmaster_xml).getroot()

        bulk_anime = []
        bulk_titles = []

        all_anime_tags = anime_titles.findall('anime')

        for anime in all_anime_tags:
            aid = anime.get('aid')
            anime_elem = anime_tvdb.find(('anime[@anidbid="%s"]' % (aid)))
            tvdb_id = anime_elem.get('tvdbid')

            try:
                int(tvdb_id)
            except ValueError:

                # Don't load any imdb movies first for now
                continue
                # Remove continue to load imdb stuff
                tvdb_id = None

            imdb_id = anime_elem.get('imdbid')

            anime_data = {
                'anidb_id': aid,
                'tvdb_id': tvdb_id,
                'imdb_id': imdb_id,
            }

            anime_model = anime_models.Anime.objects.filter(**anime_data)
            if anime_model.exists():
                anime_model = anime_model[0]
            else:
                anime_model = anime_models.Anime(**anime_data)
                bulk_anime.append(anime_model)

        anime_models.Anime.objects.bulk_create(bulk_anime)

        for anime in all_anime_tags:
            aid = anime.get('aid')
            anime_instance = anime_models.Anime.objects.filter(anidb_id=aid)

            if not anime_instance.exists():
                continue

            for title in anime:
                title_data = {
                    'type': title.get('type'),
                    'title': title.text,
                    'locale': title.get('{http://www.w3.org/XML/1998/namespace}lang'),
                    'anime': anime_instance[0],
                }

                title_model = anime_models.Title.objects.filter(**title_data)
                if not title_model.exists():
                    bulk_titles.append(anime_models.Title(**title_data))

        
        anime_models.Title.objects.bulk_create(bulk_titles)



