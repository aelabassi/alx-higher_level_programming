#!/usr/bin/python3
"""Define a sqaure class"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0) -> None:
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
