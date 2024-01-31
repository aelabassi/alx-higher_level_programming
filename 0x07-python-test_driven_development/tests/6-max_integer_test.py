#!/usr/bin/python3
"""
This module run unittests on a function that returns
the max integer in a list of integers
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class run unittests on 6-max_integer function """
    def test_integers(self):
        """ test with integers """
        result = max_integer([1, 3, 4, 5, 6])
        self.assertEqual(result, 6)
        list_1 = [2, 45, 67, 89, 23]
        self.assertEqual(max_integer(list_1), 89)

    def test_floats(self):
        """ test with floats """
        self.assertEqual(max_integer([1.0, 26.67]), 26.67)
        self.assertEqual(max_integer([0.6, 129.5]), 129.5)

    def test_ints_floats(self):
        """ test with integers and floats """
        self.assertEqual(max_integer([1, 9.8]), 9.8)
        self.assertEqual(max_integer([0.6, 2]), 2)

    def test_strings(self):
        """test with strings"""
        self.assertEqual(max_integer("Deadpool"), "p")
        self.assertEqual(max_integer("BatmanWhoLaughts"), "u")
        self.assertEqual(max_integer("Gengrey"), "y")
        self.assertEqual(max_integer("wonderwomen"), "w")
        
    def test_empty_list(self):
        """ test with empty list """
        self.assertEqual(max_integer([]), None)
        
    def test_empty_strings(self):
        """ test with empty strings """
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
