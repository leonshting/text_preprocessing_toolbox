import re
import os

from filters.BaseFilter import BaseFilter


class StaticFilter(BaseFilter):

    def __init__(self, pattern_file: str, embrace: bool=True, replace_string: str =' '):
        super(StaticFilter, self).__init__()

        self._replace_char = replace_string
        self._pattern_file = pattern_file
        self._patterns = self._load_patterns_with_file(self._pattern_file)
        self._pattern = self._make_single_pattern_w_patterns(self._patterns)
        if embrace:
            self._final_patterns = self._populate_pattern(self._pattern)
        else:
            self._final_patterns = [self._pattern]

    def filter_string(self, s: str):
        for pattern in self._final_patterns:
            if self._pattern_dict.get(pattern) is None:
                self._pattern_dict[pattern] = re.compile(pattern=pattern)
            s = self._pattern_dict[pattern].sub(string=s, repl=' {} '.format(self._replace_char))
        return s

    @classmethod
    def init_from_dict_of_params(cls, params, path):
        obj_class = cls
        obj = obj_class(
            embrace=params['embrace'],
            replace_string=params.get('replace_with'),
            pattern_file=os.path.join(path, params['file'])
        )
        return obj
