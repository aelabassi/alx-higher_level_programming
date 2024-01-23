#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """This class defines a Square"""
    def __init__(self, size=0):
        """Init a new Square
            Args:
                size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of Square"""
        return self.__size**2
