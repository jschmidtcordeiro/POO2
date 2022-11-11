import json
from parse import IParse

class JsonParser(IParse):

    def parse(self, file) -> dict:
        return json.load(file) 