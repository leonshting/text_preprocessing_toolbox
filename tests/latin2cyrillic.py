import unittest

from latin2cyrillic.Latin2Cyrillic import Latin2Cyrillic


class Latin2CyrTest(unittest.TestCase):

    def test_correct_filtering(self):
        fltr = Latin2Cyrillic()
        self.assertEqual(fltr.subs('соcискa', 'сосиска'))

if __name__ == '__main__':
    unittest.main()

