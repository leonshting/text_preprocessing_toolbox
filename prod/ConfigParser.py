import json
from functools import reduce

from filters.StaticFilter import StaticFilter
from filters.SynonymReplacer import SynonymReplacer
from helpers.small_static_rpl import *
from filters.predefined.UnicodeFilter import UnicodeFilter
from filters.predefined.MyStemWrapper import MyStemWrapper
from latin2cyrillic.Latin2Cyrillic import Latin2Cyrillic


class ConfigParser:

    def __init__(self, config_file: str):
        self._service_fields = ['BASE_DICT_DIR']
        self._filter_json_types = {
            'single_replace': StaticFilter,
            'multiple_replace': SynonymReplacer
        }
        self._predefined_filters = {
            "lower": str.lower,
            "newline_filter": rpl_newline,
            "latin_to_cyrillic": Latin2Cyrillic,
            "unicode_filter": UnicodeFilter,
            "stemmer": MyStemWrapper
        }

        try:
            with open(config_file) as f:
                self._config_dict = json.load(f)
                self._BASE_DICT_DIR = self._config_dict['config']['BASE_DICT_DIR']
                self.available_filter_params = self._config_dict['config']['available_filters']
                self.filter_order = self._config_dict['order']
        except json.JSONDecodeError or KeyError:
            print('Error on parsing config file')

        self._init_all_filters()

    def _init_filter(self, filter_name: str):
        filter_params = self.available_filter_params[filter_name]
        if filter_params['filter_kind'] == 'predefined':
            # embrace is not working for now
            return self._resolve_filter_function(self._predefined_filters[filter_name])
        else:
            obj = self._filter_json_types[filter_params['filter_kind']].init_from_dict_of_params(
                filter_params,
                self._BASE_DICT_DIR
            )
            return self._resolve_filter_function(obj=obj)

    def _init_all_filters(self):
        self.filters = []
        self.filtering_functions = []
        for name in self.filter_order:
            tmp = self._init_filter(filter_name=name)
            self.filters.append(tmp[0])
            self.filtering_functions.append(tmp[1])

    # convenience func to make each of the filtering streams have the same interface
    def _resolve_filter_function(self, obj):
        if isinstance(obj, type):
            try:
                ret_obj = obj()
                return ret_obj, ret_obj.filter_string
            except Exception:
                raise "Method filter_string not found in {}".format(obj)
        elif reduce(lambda i,j: i or isinstance(obj, j), self._filter_json_types.values(), False):
            return obj, obj.filter_string
        else:
            return None, obj

    def filter_string(self, s: str, verbose:bool=False):
        ret_str = s
        for func, name in zip(self.filtering_functions, self.filter_order):
            ret_str = func(ret_str)
            if verbose:
                print('After stage {}: {}'.format(name, ret_str))
        return ret_str