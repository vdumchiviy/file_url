from django.conf import settings
from datetime import datetime


class FormatConverter_dt():
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.strptime(value, settings.FORMAT_STRING_DT)

    def to_url(self, value):
        return value.strftime(settings.FORMAT_STRING_DT)
