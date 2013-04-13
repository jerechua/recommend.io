import datetime
from django.utils.timezone import utc

def datetime_now():
    """
    Timezone aware date time object
    """
    return datetime.datetime.utcnow().replace(tzinfo=utc)