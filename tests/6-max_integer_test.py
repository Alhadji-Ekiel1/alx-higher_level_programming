#!/usr/bin/python3
import unittest

def max_integer(lst=[]):
    # If the list is empty, return None
    if len(lst) == 0:
        return None
    
    # Initialize max_num as the first element of the list
    max_num = lst[0]
    
    # Iterate through the list to find the maximum number
    for num in lst:
        if num > max_num:
            max_num = num
    
    # Return the maximum number found
    return max_num

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        # Test that the function returns None for an empty list
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        # Test that the function returns the single element for a list with one element
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_element_list(self):
        # Test that the function returns the maximum number for a list with multiple elements
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

if __name__ == '__main__':
    unittest.main()
