#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """This class defines a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Init a new Square
            Args:
                size (int): size of the square
                position (int, int): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter: returns the size"""
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

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter: sets the position to value
            Args:
                value (tuple):tuple of ints to set position to
        """
        if (not isinstance(value, tuple) or
                not all(isinstance(v, int) for v in value) or
                len(value) != 2 or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of square"""
        return self.__size**2

    def my_print(self):
        """prints the square using #"""
        if self.__size == 0:
            print("")
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end='')
            for _ in range(self.__size):
                print("#", end='')
            print("")
