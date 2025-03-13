import unittest
from search_algorithms import linear_search, binary_search, ternary_search

class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 3), 2)
        self.assertEqual(linear_search(arr, 6), -1)

    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)
        self.assertEqual(binary_search(arr, 6), -1)

    def test_ternary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ternary_search(arr, 3), 2)
        self.assertEqual(ternary_search(arr, 6), -1)

if __name__ == '__main__':
    unittest.main()