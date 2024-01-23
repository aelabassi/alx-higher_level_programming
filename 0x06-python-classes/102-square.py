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

    def __eq__(self, other: object) -> bool:
        """compares two areas of two Square instances"""
        return self.area() == other.area()

    def __ne__(self, other: object) -> bool:
        """Difference between two Square instances"""
        return self.area() != other.area()

    def __gt__(self, other: object) -> bool:
        """is self's area is greater than other's"""
        return self.area() > other.area()

    def __ge__(self, other: object) -> bool:
        """is self's area is greater or equal than other's"""
        return self.area() >= other.area()

    def __lt__(self, other: object) -> bool:
        """is self's area is less than other's"""
        return self.area() < other.area()

    def __le__(self, other: object) -> bool:
        """is self's area is less or equal than other's"""
        return self.area() <= other.area()
