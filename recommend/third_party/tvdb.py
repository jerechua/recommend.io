from base_integration import BaseIntegration

from django.conf import settings
from django.core.files.storage import default_storage

from django_boto.s3 import upload

from xml.etree import ElementTree

import requests
import urllib
import os


class Tvdb(BaseIntegration):

    BASE_URL = settings.API_KEYS['tvdb']['base_url']
    META_URL = settings.API_KEYS['tvdb']['meta_url']
    API_KEY = settings.API_KEYS['tvdb']['api_key']

    def get_series_by_id(self, anime_model):
        api_endpoint = '%s/series/%s/' % (self.API_KEY, repr(anime_model.tvdb_id))
        response = self.get_request(api_endpoint)
        return self._parse_xml_data(response, anime_model)

    def _parse_xml_data(self, response, anime_model):
        assert(response.status_code == 200, "XML Data is invalid")

        xml = ElementTree.fromstring(response.content)

        xml_data = {}
        xml_data['description'] = xml.find('.//Overview').text
        xml_data['network'] = xml.find('.//Network').text
        xml_data['imdb_id'] = xml.find('.//IMDB_ID').text
        xml_data['first_aired'] = xml.find('.//FirstAired').text

        genres = xml.find('.//Genre').text
        xml_data['genre'] = genres.strip('|').split('|')

        xml_data['banner_url'] = self._save_photo(xml.find('.//banner').text)
        xml_data['poster_url'] = self._save_photo(xml.find('.//poster').text)
        xml_data['fanart_url'] = self._save_photo(xml.find('.//fanart').text)

        return xml_data

    def _save_photo(self, url):

        file_path = "%s%s" % (settings.IMAGE_DIR, url)
        dir_path = os.path.dirname(file_path)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        f = open(file_path ,'wb')
        f.write(urllib.urlopen(settings.API_KEYS['tvdb']['meta_url'] + url).read())
        f.close()

        f = open(file_path, 'r')

        upload(f)

        f.close()

        return f.name


