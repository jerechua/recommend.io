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
        if self.request.user.is_authenticated():
            required['sessionid'] = self.request.session.session_key

        return required

    def datetime_now():
        """
        Figures out the django time aware object
        """
        return time.datetime_now().strftime("%d_%m_%Y_%H_%M_%S")


    def send_default_action(
            self, default_action, item_id, rating, item_description, item_url,
            user_id=None, item_image_url=None, action_time=datetime_now(), item_type=None):
        """
        Send a default action to easyrec recommend engine. Default actions are rate, view, and buy
        """

        default_actions = ['rate', 'view', 'buy']
        assert (default_action in default_actions, "Only default actions allowed")

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

        response = self.get_request(default_action, **data)

    def send_custom_action(
            self, action_type, item_id, rating, item_description, item_url,
            action_value=None, user_id=None, item_image_url=None, action_time=datetime_now(), item_type=None):
        """
        send a custom action to easyrec. Custom actions need to be activated on the engine before
        it can be used
        """

        data = {
            'itemid': item_id,
            'rating': rating,
            'itemdescription': item_description,
            'itemurl': item_url,
            'actiontype': action_type,
            'actionvalue': action_value,
            'userid': user_id,
            'itemimageurl': item_image_url,
            'actiontime': action_time,
            'itemtype': item_type,
        }

        response = self.get_request('sendaction', **data)
