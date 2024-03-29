#!/usr/bin/python3
"""
Rectangle class inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGoemetry """
    def __init__(self, width, height):
        """ Init a new Rectangle instance """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width*self.__height

    def __str__(self):
        """__str__ overloading"""
        class_name = "[" + str(self.__class__.__name__) + "] "
        class_name += str(self.__width) + "/" + str(self.__height)
        return class_name
