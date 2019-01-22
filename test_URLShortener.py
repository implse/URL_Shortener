import unittest
import random
from URLShortener import URL_shortener

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.url = URL_shortener()
        self.url_short = self.url.shorten("https://github.com/implse")
        self.url_restore = self.url.restore(self.url_short)

    def test_SelectionSort(self):

        self.assertIsInstance(self.url, URL_shortener)
        self.assertEqual(len(self.url_short), 22)
        self.assertEqual(self.url_restore, "https://github.com/implse")

        # Check cache : same URL twice (re-use suffix)
        suffix = self.url_short[-6:]
        self.url_short = self.url.shorten("https://github.com/implse")
        self.assertEqual(suffix, self.url_short[-6:] )

if __name__ == '__main__':
    unittest.main()
