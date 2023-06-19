import json

from domain.driver import Driver
from domain.race import Race


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Race):
            return obj.__dict__
        if isinstance(obj, Driver):
            return obj.__dict__
        return super().default(obj)
