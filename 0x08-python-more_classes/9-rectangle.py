#!/usr/bin/python3
"""
This module defines a rectangle class
"""


class Rectangle:
    """This class defines a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Initialize a rectangle instance
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method that compares the area of the two rectangles
            Args:
                rect_1 (Rectangle): first rectangle
                rect_2 (Rectangle): second rectangle
            Returns: rectangle with the biggest area
                    rect_1 if they have the same area
            Raises:
                TypeError: rect_1 and rect_2 must be an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ class method that returns an new Rectangle instance with
        width == height == size
        """
        return cls(size, size)

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height*self.__width

    def perimeter(self):
        """ Calculate the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2*(self.__height + self.__width)

    def print(self):
        """Print the rectangle using #"""
        if self.__height == 0 or self.__width == 0:
            print()
        for _ in range(self.__height):
            for _ in range(self.__width):
                print(self.print_symbol, end='')
            print()

    def __str__(self):
        """ instance print method (operator<<) """
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ""

        for i in range(self.__height):
            for _ in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self) -> str:
        "Return the constructor form of the instance"
        new_rectangle = f"Rectangle({str(self.__width)}, {str(self.__height)})"
        return new_rectangle

    def __del__(self):
        """ destructor of the class """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
