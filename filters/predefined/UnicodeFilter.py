import unicodedata


class UnicodeFilter:

    def __init__(self):
        string = '`1234567890-~!@#$%^&*()_+qwertyuiop[]\asdfghjkl;QWERTYUIOP{}| ' + \
                 '`1234567890-~!@#$%^&*()_+йцукенгшщзхъёфывапролджэячсмитьбю/ЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮ?' + \
                 '[!"№%:,.;()_+]'
        categories = []

        for i in string:
            categories.append(unicodedata.category(i))
        self._available_categories = set(categories)

    def filter_string(self, s: str):
        return ''.join([i for i in s if unicodedata.category(i) in self._available_categories])