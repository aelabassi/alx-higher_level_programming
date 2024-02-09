#!/usr/bin/python3
"""
Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init a new Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter: sets the width to size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter: sets the values of with anf height"""
        self.width = value
        self.height = value

    def __str__(self):
        """Square str method"""
        str_ = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} "
        str_ += f"- {self.size}"
        return str_
