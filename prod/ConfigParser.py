import json
from filters.StaticFilter import StaticFilter


class ConfigParser:

    def __init__(self, config_file: str):
        self._service_fields = ['BASE_DICT_DIR']
        self._filter_json_types = {
            'single_replace': StaticFilter,
            'key_replace': None
        }

        try:
            with open(config_file) as f:
                self.config_dict = json.load(f)
                self.BASE_DICT_DIR = self.config_dict['BASE_DICT_DIR']
        except json.JSONDecodeError or KeyError:
            print('Error on parsing config file')

        self._set_filters()

    def _set_filters(self):
        self._filters = [i for i in self.config_dict.keys() if i not in self._service_fields]

    def _init_filters(self):
        pass
