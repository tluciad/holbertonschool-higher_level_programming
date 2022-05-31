#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer"""

    def test_max_integer1(self):
        """first test to evaluate the max integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 8, 9, 2]), 9)

    def text_max_integer2(self):
        """to check that the list is not empty"""
        self.assertEqual(max_integer([]), None)

    def text_max_integer3(self):
        """to check with negatives in the list """
        self.assertEqual(max_integer([-50, -7, 8, 3]), 8)
        self.assertEqual(max_integer([-50, -7, -8, -3]), -3)

    def text_max_integer4(self):
        """to check with floats in the list"""
        self.assertEqual(max_integer([-50.5, -7.2, 8, 3.5, 9]), 9)
        self.assertEqual(max_integer([-50, -7.3, -8.2, -3.1]), -3.1)
    
    def text_max_integer5(self):
        """to check max at the beggining"""
        self.assertEqual(max_integer([12, 3, 1, 4]), 12)
        self.assertEqual(max_integer([-1, -7.3, -8.2, -3.1]), -1)

    def text_max_integer6(self):
        """to check max list with one element"""
        self.assertEqual(max_integer([8]), 8)
    
    def text_max_integer7(self):
        """to check max just negatives integers"""
        self.assertEqual(max_integer([-12, -3, -1, -4]), -1)
        self.assertEqual(max_integer([-7, -2, -5]), -2)
      
    def text_max_integer8(self):
        """to check max one negativein list"""
        self.assertEqual(max_integer([-12, 3, 1, 4]), 4)
       


if __name__ == '__main__':
    unittest.main()
