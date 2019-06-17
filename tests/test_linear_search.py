import unittest

from Searching.linear_search import LinearSearch


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.lot = [2, 10, 30, 32, 33, 78, 98, 101]
        self.linear_search = LinearSearch(self.lot)

    def test_linear_search_finds_an_element(self):
        self.assertTrue((True, 5), self.linear_search.search(78))
        self.assertTrue((True, 0), self.linear_search.search(2))
        self.assertTrue((True, 6), self.linear_search.search(98))
        self.assertTrue((True, 7), self.linear_search.search(101))

    def test_linear_search_does_not_find_an_element(self):
        self.assertEqual((False, -1), self.linear_search.search(4))
        self.assertEqual((False, -1), self.linear_search.search(102))
        self.assertEqual((False, -1), self.linear_search.search(1))
