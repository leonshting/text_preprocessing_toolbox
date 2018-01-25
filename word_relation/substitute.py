import json
import os
from collections import defaultdict

from preprocessing.prod.dict_parsers.GraphDictParser import GraphDictParser


class BaseGraphSubstitute:
    def __init__(self, config_file: str):
        self.parser = GraphDictParser
        self._files = self.get_graphed_dicts(config_file)
        self._graphs = [GraphDictParser(filename=file).get_graph() for file in self._files]
        self._types = [GraphDictParser(filename=file).get_types() for file in self._files]

    @staticmethod
    def get_graphed_dicts(file: str):
        with open(file) as f:
            config = json.load(f)['config']
            filters = config['available_filters']

        return [os.path.join(config['BASE_DICT_DIR'], v['file'])
                for k, v in filters.items() if v.get('graphed') is not None]

    @property
    def graphs(self):
        return self._graphs

    @property
    def types(self):
        return self._types


class DeepestGraphSubstitute(BaseGraphSubstitute):
    def __init__(self, config_file: str):
        super(DeepestGraphSubstitute, self).__init__(config_file=config_file)

    def subs_string(self, tokenized_string: str):
        ret = tokenized_string.split()
        for _type in self.types:
            ret = [_type.get(word, word) for word in ret]
        return " ".join(ret)

    def subs_dict(self, tokenized_string: str):
        ret = tokenized_string.split()
        ret_dict = defaultdict(list)
        for _type in self.types:
            tmp_dict = defaultdict(list)
            for word in ret:
                if _type.get(word) is not None:
                    tmp_dict[_type.get(word)].append(word)
            ret_dict.update(tmp_dict)
        return ret_dict


class ClosestGraphSubstitute(BaseGraphSubstitute):
    def __init__(self, config_file):
        super(ClosestGraphSubstitute, self).__init__(config_file=config_file)

    def subs_string(self, tokenized_string: str):
        # pass
        return tokenized_string
