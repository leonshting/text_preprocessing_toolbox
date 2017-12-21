def alphabet(lang='rus') -> str:
    first_last_chars = {'rus': 'ая', 'eng': 'az'}
    return ''.join([chr(i) for i in range(ord(first_last_chars[lang][0]), ord(first_last_chars[lang][1])+1)])