#!/usr/bin/python3
"""
This module have a MyList class
"""


class MyList(list):
    """This class inherit from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
