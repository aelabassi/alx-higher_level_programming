#!/usr/bin/python3
"""
Improved BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def __init__(self):
        pass

    def area(self):
        """area of the some geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value variable
            Args:
                name: (string)
                value: (int)
            Raises:
                TypeError: value must be an int
                ValueError: value must be > 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
