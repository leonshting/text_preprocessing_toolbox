import re
import json


class StaticFilter():

    def __init__(self, pattern_file:str):
        self._pattern_file = pattern_file
        self._load_patterns()
        self._make_single_pattern()

    def _load_patterns(self):
        with open(self._pattern_file) as f:
            self._patterns = json.load(f)

    def _make_single_pattern(self):
        self._pattern = '|'.join(['({})'.format(p) for p in self._patterns])

    def filter_string(self, s: str):
        tmp = re.sub(pattern=self.pattern, string=s, repl=' ')
        return tmp
