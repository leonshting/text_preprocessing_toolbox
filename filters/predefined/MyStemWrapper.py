from pymystem3 import Mystem


class MyStemWrapper:
    def __init__(self, join_string: str=''):
        self._join_string = join_string
        self._stemmer = Mystem()

    def filter_string(self, s: str):
        return self._join_string.join(self._stemmer.lemmatize(s)[:-1])