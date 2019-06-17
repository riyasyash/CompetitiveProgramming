import unittest

from Searching.BinarySearch import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.lot = [2, 10, 30, 32, 33, 78, 98, 101]
        self.binary_search = BinarySearch(self.lot)

    def test_binary_search_finds_an_element(self):
        self.assertTrue((True, 5), self.binary_search.search(78))
        self.assertTrue((True, 0), self.binary_search.search(2))
        self.assertTrue((True, 6), self.binary_search.search(98))
        self.assertTrue((True, 7), self.binary_search.search(101))

    def test_binary_search_does_not_find_an_element(self):
        self.assertEqual((False, -1), self.binary_search.search(4))
        self.assertEqual((False, -1), self.binary_search.search(102))
        self.assertEqual((False, -1), self.binary_search.search(1))
