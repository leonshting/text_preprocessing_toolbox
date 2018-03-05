from preprocessing.prod.dict_parsers.BaseDictParser import BaseDictParser


class GraphDictParser(BaseDictParser):
    def __init__(self, filename, synonym_field='synonyms', type_field='type',
                 tokens_field='tokens', parents_field='parents', features_field='features'):
        super(GraphDictParser, self).__init__(filename=filename)
        self._synonym_field = synonym_field
        self._type_field = type_field
        self._tokens_field = tokens_field
        self._parents_field = parents_field
        self._features_field = features_field
        self._dict = {}
        self._graph = {}
        self._types = {}
        self._feat_map = {}
        self._inverse_feat_map = {}

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

    def get_feat_graph(self):
        if len(self._feat_map) == 0:
            for k, v in self.loaded[self._tokens_field].items():
                if v.get(self._features_field) is not None:
                    self._feat_map[k] = v.get(self._features_field)
                    for f in v.get(self._features_field):
                        self._inverse_feat_map[f] = k
        return self._feat_map

    def get_types(self):
        if len(self._types) == 0:
            for k, v in self.loaded[self._tokens_field].items():
                self._types[k] = self.loaded[self._type_field]
        return self._types