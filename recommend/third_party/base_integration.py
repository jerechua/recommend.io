import urllib

from django.conf import settings


class BaseUrlNotDefined(Exception):
    pass


class BaseIntegration:

    """
    Used to create the base api calls to third party apis
    """

    BASE_URL = ''

    def __init__(self, request=None):
        self.request = request

    def get_static_fields(self):
        """
        For any static params/auth needed
        """

        return {}

    def get_request(self, api_endpoint, **kwargs):
        """
        Does the request
        """

        if not self.BASE_URL:
            raise BaseUrlNotDefined()

        # Join the requried params with the parameters
        kwargs.update(self.get_static_fields())

        # convert to querystring
        params = urllib.urlencode(kwargs)

        url = "%s%s?%s" % (self.BASE_URL, api_endpoint, params)
        print url

    def post_request(self, api_endpoint, **kwargs):

        raise NotImplementedError()
