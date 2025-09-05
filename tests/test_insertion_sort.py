import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_basic_sort(self):
        """Test sorting a simple unsorted list."""
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_sorted_list(self):
        """Test sorting an already sorted list."""
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test sorting a reverse-sorted list."""
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        """Test sorting a list with duplicate elements."""
        self.assertEqual(insertion_sort([5, 2, 9, 1, 5, 6, 2]), [1, 2, 2, 5, 5, 6, 9])

    def test_empty_list(self):
        """Test sorting an empty list."""
        self.assertEqual(insertion_sort([]), [])

    def test_single_element_list(self):
        """Test sorting a list with a single element."""
        self.assertEqual(insertion_sort([42]), [42])

    def test_list_with_negative_numbers(self):
        """Test sorting a list containing negative numbers."""
        self.assertEqual(insertion_sort([-5, -2, -9, -1, -5, -6]), [-9, -6, -5, -5, -2, -1])

    def test_list_with_mixed_numbers(self):
        """Test sorting a list with positive, negative, and zero."""
        self.assertEqual(insertion_sort([3, -1, 0, 5, -2]), [-2, -1, 0, 3, 5])

if __name__ == '__main__':
    unittest.main()
