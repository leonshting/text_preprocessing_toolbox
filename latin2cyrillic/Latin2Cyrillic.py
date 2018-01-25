import numpy as np

from preprocessing.helpers.for_strings import alphabet


class Latin2Cyrillic:
    """now the class replaces latin characters with russian analogs and does not the inverse"""
    def __init__(self):
        self._cyr_lat_map = {'а': 'a', 'е': 'e', 'к': 'k', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y'}
        self._lat_cyr_map = {v: k for k, v in self._cyr_lat_map.items()}

        self.cyr_alphabet = alphabet(lang='rus')
        self.eng_alphabet = alphabet(lang='eng')

        self.from_lat_translator = str.maketrans(self._lat_cyr_map)
        self.from_cyr_translator = str.maketrans(self._cyr_lat_map)

    def _word_cyr_lat_occurrence(self, word: str, cyrillic_first=True):
        """counts occurrence of latin and cyrillic characters"""
        cnt = np.zeros(2)
        cyr_index = 0 if cyrillic_first else 1
        lat_index = 1 - cyr_index
        for char in word:
            if char in self.cyr_alphabet:
                cnt[cyr_index] += 1
            elif char in self.eng_alphabet:
                cnt[lat_index] += 1
        return cnt

    def subs(self, word: str, threshold=0.5):
        """perform substitution if the share of cyrillic symbols is greater than threshold"""
        cnt = self._word_cyr_lat_occurrence(word=word, cyrillic_first=True)
        length_significant = cnt.sum()

        if cnt[0]/(length_significant+0.01) > threshold:
            return self._subs_latin_with_cyrillic(word=word)
        else:
            return word

    def filter_string(self, s:str):
        return " ".join([self.subs(i) for i in s.split()])

    def _subs_latin_with_cyrillic(self, word: str):
        """perform substitution of latin characters"""
        return word.translate(self.from_lat_translator)

