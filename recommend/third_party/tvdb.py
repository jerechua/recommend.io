from base_integration import BaseIntegration

from django.conf import settings

from xml.etree import ElementTree


class Tvdb(BaseIntegration):

    BASE_URL = settings.API_KEYS['tvdb']['base_url']
    META_URL = settings.API_KEYS['tvdb']['meta_url']
    API_KEY = settings.API_KEYS['tvdb']['api_key']

    def get_series_by_id(self, tvdb_id):
        api_endpoint = '%s/series/%s/' % (self.API_KEY, repr(tvdb_id))
        response = self.get_request(api_endpoint)
        return self._parse_xml_data(response)

    def _parse_xml_data(self, response):
        assert(response.status_code == 200, "XML Data is invalid")

        xml = ElementTree.fromstring(response.content)

        xml_data = {}
        xml_data['description'] = xml.find('.//Overview').text
        xml_data['network'] = xml.find('.//Network').text
        xml_data['imdb_id'] = xml.find('.//IMDB_ID').text
        xml_data['first_aired'] = xml.find('.//FirstAired').text

        genres = xml.find('.//Genre').text
        xml_data['genre'] = genres.strip('|').split('|')

        xml_data['banner_url'] = xml.find('.//banner').text
        xml_data['poster_url'] = xml.find('.//poster').text
        xml_data['fanart_url'] = xml.find('.//fanart').text

        return xml_data

