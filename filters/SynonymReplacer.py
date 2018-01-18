import re
import json
import os

from filters.BaseFilter import BaseFilter
from collections import OrderedDict


class SynonymReplacer(BaseFilter):

    def __init__(self, pattern_file: str, embrace: bool=True, rpl_w_token: bool=True,
                 token_file: str=None, graphed: bool=False):
        super(SynonymReplacer, self).__init__()
        self._embrace = embrace
        self._pattern_file = pattern_file
        self._rpl_w_token = rpl_w_token
        self._graphed_file = graphed
        if self._rpl_w_token:
            if token_file is not None:
                with open(token_file, 'r') as f:
                    self._token_dict = json.load(f, object_pairs_hook=OrderedDict)
            else:
                raise Exception('if replacing with token is true, token file must be provided')
        self._patterns = self._load_patterns_with_file(self._pattern_file, kind='graph' if graphed else 'base')
        self._final_pattern_dict = self._make_single_pattern_dict(self._patterns)

    def _make_single_pattern_dict(self, pattern_dict):
        if self._embrace:
            return {k: self._populate_pattern(self._make_single_pattern_w_patterns(v)) for k, v in pattern_dict.items()}
        else:
            return {k: [self._make_single_pattern_w_patterns(v)] for k, v in pattern_dict.items()}

    def filter_string(self, s: str):
        for k, pattern_list in self._final_pattern_dict.items():
            to_rpl = k
            if self._rpl_w_token:
                to_rpl = self._token_dict.get(k, to_rpl)
                # pattern_list.append(k)
            to_rpl = ' {} '.format(to_rpl)
            for pattern in pattern_list:
                if self._pattern_dict.get((k, pattern)) is None:
                    self._pattern_dict[(k, pattern)] = re.compile(pattern)
                s = self._pattern_dict[(k, pattern)].sub(repl=to_rpl, string=s)
        return s

    @classmethod
    def init_from_dict_of_params(cls, params, path):
        rpl_w_token_param = 'word_to_token_file' in params.keys()
        token_file = os.path.join(path, params['word_to_token_file']) if rpl_w_token_param else None
        obj = cls(
            embrace=params['embrace'],
            pattern_file=os.path.join(path, params['file']),
            rpl_w_token=rpl_w_token_param,
            token_file=token_file,
            graphed=params.get('graphed', False)
        )

        return obj
