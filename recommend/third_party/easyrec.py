from django.conf import settings
from base_integration import BaseIntegration

from utils import time


class Easyrec(BaseIntegration):

    DEFAULT_SESSION_ID = 'default_user_session_id'
    BASE_URL = settings.API_KEYS['easyrec']['base_url'] + "api/1.0/"

    def get_static_fields(self):
        required = {}
        required['apikey'] = settings.API_KEYS['easyrec']['api_key']
        required['tenantid'] = settings.API_KEYS['easyrec']['tenant_id']

        required['sessionid'] = self.DEFAULT_SESSION_ID
        if self.request.is_authenticated():
            required['sessionid'] = self.request.session.session_key

        return required

    def get_fields(self):
        return {}

    def send_rate(self, item_id, rating, item_description, item_url,
                  user_id=None, item_image_url=None, action_time=time.datetime_now(), item_type=None):

        endpoint = "rate"

        data = {
            'itemid': item_id,
            'rating': rating,
            'itemdescription': item_description,
            'itemurl': item_url,
            'userid': user_id,
            'itemimageurl': item_image_url,
            'actiontime': action_time,
            'itemtype': item_type,
        }

        response = self.send_request(endpoint, **data)



x = Easyrec()
x.send_rate(1, 1, "Asdf", "123", "456", 'http', 'time', 'type')
