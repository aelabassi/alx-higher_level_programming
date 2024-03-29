#!/usr/bin/python3
"""
Square class inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from BaseGoemetry """
    def __init__(self, size):
        """ Init a new Square instance """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of rectangle"""
        return self.__size*self.__size

    def __str__(self):
        class_name = "[" + str(self.__class__.__name__) + "] "
        class_name += str(self.__size) + "/" + str(self.__size)
        return class_name
