#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """This class defines a square"""
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

    @property
    def size(self):
        """getter: get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: set the value of size to value
            Args:
                value (int): value to set size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
