#!/usr/bin/python3
"""
This function adds two non-Non integer types
"""


def add_integer(a, b=98):
    """This function returns the sum of a and b
        Args:
            a (int): first int
            b (int): second int
        Return:
            a + b (int): sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a)+int(b)
