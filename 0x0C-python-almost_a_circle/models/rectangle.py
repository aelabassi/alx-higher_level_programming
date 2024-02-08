#!/usr/bin/python3
"""
Rectangle class inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a rectangle instances"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter: returns the with"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: set the value of the width"""
        self.__width = value

    @property
    def height(self):
        """getter: returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets the value of height"""
        self.__height = value
