import unittest

from Arrays.missing_number import MissingNumberEvaluator


class TestMissingNumberEvaluator(unittest.TestCase):
    def setUp(self):
        self.array1 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
        self.array2 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
        self.array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.array4 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

    def test_find_missing(self):
        self.assertEqual(MissingNumberEvaluator(array=self.array1).find_missing(), 5)
        self.assertEqual(MissingNumberEvaluator(array=self.array2).find_missing(), 7)
        self.assertEqual(MissingNumberEvaluator(array=self.array3).find_missing(), 10)
        self.assertEqual(MissingNumberEvaluator(array=self.array4).find_missing(), 4)
