from itertools import product

from preprocessing.prod.dict_parsers.GraphDictParser import GraphDictParser
from preprocessing.prod.dict_parsers.BaseDictParser import BaseDictParser

dict_parsers = {
    'base': BaseDictParser,
    'graph': GraphDictParser
}


class BaseFilter:

    def __init__(self):
        self._beginning_separators = [
            self.construct_named_regex(name='begin',
                                       pattern=pattern,
                                       after_group_quantifier=quantifier,
                                       string_beginning=string_beginning)
            for pattern, string_beginning, quantifier in zip([r"[\s\(]", r"[\?!,\.\(\)\s]"], [True, False], ['*', '+'])
        ]
        self._ending_separators = [
            self.construct_named_regex(name='end',
                                       pattern=r"[\?!,\.\(\)\s]",
                                       after_group_quantifier=quantifier,
                                       string_ending=string_ending)
            for quantifier, string_ending in zip(["*", "+"], [True, False])
        ]
        self._pattern_dict = {}

    @staticmethod
    def construct_named_regex(name: str, pattern: str, after_group_quantifier: str='?',
                              string_beginning=False, string_ending=False):
        string_b = '^' if string_beginning else ''
        string_e = '$' if string_ending else ''
        return r"{}(?P<{}>{}){}{}".format(string_b, name, pattern, after_group_quantifier, string_e)

    @staticmethod
    def _load_patterns_with_file(pattern_file, kind='base'):
        return dict_parsers[kind](pattern_file).get_dict()

    @staticmethod
    def _make_single_pattern_w_patterns(patterns):
        return '({})'.format('|'.join(['({})'.format(p) for p in patterns]))

    def _populate_pattern(self, pattern):
        """embraces pattern with:
            1. beginning of string & end of string
            2. space & end of string
            3. beginning of string & space
            4. space & end of sentence
        """
        return [begin + pattern + end for begin, end in product(self._beginning_separators, self._ending_separators)]