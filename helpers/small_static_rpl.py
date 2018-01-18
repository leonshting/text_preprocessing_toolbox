import re


def lower(string):
    return string.lower()


def rm_stop_phrases(s, stop_phrases):
    for phrase in stop_phrases:
        s = re.sub(phrase, "", s, flags=re.IGNORECASE)
    return s


def rm_stop_words(s, stop_words):
    return " ".join([i for i in s.split(' ') if i not in stop_words])


def rpl_newline(s):
    return re.sub(pattern=r'[\t\n]', repl=' ', string=s)


def rm_spaces(s):
    return re.sub(pattern=r'[ -]', string=s, repl='')


def rpl_url(s):
    rg = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
    return re.sub(pattern=rg, repl=' <url> ', string=s)


def rpl_cyr_analogs(s):
    return s.replace('ё', 'е')