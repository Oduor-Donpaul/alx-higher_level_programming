#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """Test with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_number(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_both_negative_and_positive(self):
        """est with a list of both positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_list_with_single_int(self):
        """Test with a list containing a single integer"""
        self.assertEqual(max_integer([5]), 5)

    def test_mixture_of_ints_and_floats(self):
        """Test with a list containing a mixture of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 5.1]), 5.1)

    def test_duplicate_ints(self):
        """Test with a list containing duplicate integers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()
