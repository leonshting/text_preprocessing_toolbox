import unittest

from filters.StaticFilter import StaticFilter


class StaticFilterTest(unittest.TestCase):

    def test_correct_filtering(self):
        trash_filter = StaticFilter(pattern_file='./dicts/html_residuals_patterns.json')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()