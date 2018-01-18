import json

from prod.dict_parsers.BaseDictParser import BaseDictParser


class GraphDictParser(BaseDictParser):
    def __init__(self, filename, synonym_field='synonyms',
                 type_field='type', tokens_field='tokens', parents_field='parents'):
        super(GraphDictParser, self).__init__(filename=filename)
        self._synonym_field = synonym_field
        self._type_field=type_field
        self._tokens_field=tokens_field
        self._parents_field = parents_field
        self._dict = {}
        self._graph = {}

    def get_dict(self):
        if len(self._dict) == 0:
            for k, v in self.loaded[self._tokens_field].items():
                self._dict[k] = v[self._synonym_field]
        return self._dict

    def get_graph(self):
        if len(self._graph) == 0:
            for k, v in self.loaded[self._tokens_field].items():
                self._graph[k] = v[self._parents_field]
        return self._graph
