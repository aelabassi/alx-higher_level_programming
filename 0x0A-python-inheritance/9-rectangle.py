#!/usr/bin/python3
"""
Rectangle class inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGoemetry """
    def __init__(self, width, height):
        """ Init a new Rectangle instance """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width*self.__height

    def print(self):
        """print method"""
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        """__str__ overloading"""
        return f"[Rectangle] {self.__width}/{self.__height}"
