import urllib

from django.conf import settings

class BaseUrlNotDefined(Exception):
    pass

class BaseIntegration:
    """
    Used to create the base api calls to third party apis
    """

    DEFAULT_USER = 'recommend_user'
    BASE_URL = ''

    def get_static_fields(self):
        """
        For any static params/auth needed
        """

        return {}

    def get_fields(self):
        """
        for params that need to be passed
        """

        return {}

    def send_request(self, api_endpoint, **kwargs):
        """
        Does the request
        """

        if not self.BASE_URL:
            raise BaseUrlNotDefined()

        params = urllib.urlencode(kwargs)

        url = "%s%s?%s" % (self.BASE_URL, api_endpoint, params)
        print url