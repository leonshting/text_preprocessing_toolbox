from latin2cyrillic.Latin2Cyrillic import Latin2Cyrillic

lat2cyr = Latin2Cyrillic()

assert lat2cyr.subs('соcискa') == 'сосиска'
