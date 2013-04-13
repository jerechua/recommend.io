from django.conf import settings

class BaseIntegration:
    """
    Used to create the base api calls to third party apis
    """

    def _add_required_fields(url):
        """
        For any static params/auth needed
        """
        return url

    def make_request(url):
        """
        Does the request
        """
        
        pass