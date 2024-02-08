#!/usr/bin/python3
"""
Rectangle class inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a rectangle instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter: returns the with"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of with
            Args:
                value: (int)
            Raises:
                TypeError: width mst be an integer
                ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter: returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height
            Args:
                value: (int)
            Raises:
                TypeError: height mst be an integer
                ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter: returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x
            Args:
                value: (int)
            Raises:
                TypeError: x mst be an integer
                ValueError: x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """getter: returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
            Args:
                value: (int)
            Raises:
                TypeError: y mst be an integer
                ValueError: y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using #"""
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """__str__ method"""
        str_ = f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return str_
