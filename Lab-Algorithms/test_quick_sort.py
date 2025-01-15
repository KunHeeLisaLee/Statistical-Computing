import unittest
from quick_sort import apply_quick_sort


class TestQuickSOrt(unittest.TestCase):
    def test_empty_list(self):  # test when input is empty list
        self.assertEqual(apply_quick_sort([]), [])

    def test_sorted_list(self):  # test when input is already sorted
        self.assertEqual(apply_quick_sort([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_floats(self):  # test when input is floats
        self.assertEqual(apply_quick_sort([1.3, 4, 3.5, 2]), [1.3, 2, 3.5, 4])


if __name__ == '__main__':
    unittest.main()
