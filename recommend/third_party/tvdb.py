from base_integration import BaseIntegration

from django.conf import settings
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from django_boto.s3 import upload

from xml.etree import ElementTree

import requests
import urllib2
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
        if genres:
            xml_data['genre'] = genres.strip('|').split('|')

        xml_data['banner_url'] = self._save_photo(xml.find('.//banner').text)
        xml_data['poster_url'] = self._save_photo(xml.find('.//poster').text)
        xml_data['fanart_url'] = self._save_photo(xml.find('.//fanart').text)

        return xml_data

    def _save_photo(self, url):
        if url is None:
            return None

        file_path = "%s%s" % (settings.IMAGE_DIR, url)
        dir_path = os.path.dirname(file_path)

        _url = settings.API_KEYS['tvdb']['meta_url'] + url

        temp_img = NamedTemporaryFile()
        temp_img.write(urllib2.urlopen(_url).read())
        temp_img.flush()

        # image_field.save(url, File(temp_img))
        return [url, File(temp_img)]
        


