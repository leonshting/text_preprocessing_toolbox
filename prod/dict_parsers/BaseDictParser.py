import json


class BaseDictParser:
    def __init__(self, filename):
        self._filename = filename
        with open(self._filename, 'r') as f:
            self.loaded = json.load(f)
        self._dict = None

    def get_dict(self):
        return self.loaded
