#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """This class defines a Square"""
    def __init__(self, size=0):
        """Init a new Square
            Args:
                size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """getter: returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: set the value of size to value
            Args:
                value (int): value to size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size**2

    def my_print(self):
        """prints the area with #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for _ in range(self.__size):
                print("#", end='')
            print()
