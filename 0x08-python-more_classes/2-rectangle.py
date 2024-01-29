#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """This class defines a rectangle class"""
    def __init__(self, width=0, height=0) -> None:
        """Initialize a rectangle instance
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter: returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter: set the value of the width to value
            Args:
                value (int): wdith's value
            Raises:
                TypeError: value must be an integer
                ValueError: for negative values
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height to value
        Args:
            value (int): height's value
        Raises:
            TypeError: if value is not an integer
            ValueError: for negative values
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height*self.__width

    def perimeter(self):
        """ Calculate the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2*(self.__height + self.__width)
