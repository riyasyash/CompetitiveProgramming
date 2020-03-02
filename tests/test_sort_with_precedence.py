import unittest

from Sorting.sort_with_presedence import SortWithPrecedence


class TestSortWithPrecedence(unittest.TestCase):
    def setUp(self):
        self.listA_1 = [3, 4, 7, 8, 1, 3]
        self.listB_1 = [8, 3, 6, 10]

        self.listA_2 = [3, 4, 7, 8, 1, 3]
        self.listB_2 = [4, 3, 6, 1]

        self.listA_3 = [3, 4, 7, 7, 1, 3]
        self.listB_3 = [8, 7, 6, 10]

    def test_sort(self):
        self.assertEqual([8, 3, 3, 1, 4, 7], SortWithPrecedence(self.listA_1, self.listB_1).sort())
        self.assertEqual([4, 3, 3, 1, 7, 8], SortWithPrecedence(self.listA_2, self.listB_2).sort())
        self.assertEqual([7, 7, 1, 3, 3, 4], SortWithPrecedence(self.listA_3, self.listB_3).sort())
