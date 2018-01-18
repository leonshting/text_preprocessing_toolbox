import unittest

from filters.predefined import UnicodeFilter


class UnicodeFilterTest(unittest.TestCase):

    def test_correct_filtering(self):
        fltr = UnicodeFilter.UnicodeFilter()
        self.assertEqual(fltr.filter_string('\ufeff попоопп=о'), 'попоопп=о')

if __name__ == '__main__':
    unittest.main()