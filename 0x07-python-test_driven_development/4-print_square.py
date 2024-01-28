#!/usr/bin/python3
"""
This module have a function that prints a square using #

"""


def print_square(size):
    """
    Prints a square of size `size` using #
    Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
