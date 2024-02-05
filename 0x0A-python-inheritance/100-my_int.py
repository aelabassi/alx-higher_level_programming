#!/usr/bin/python3
"""
My integer inherits from int
"""


class MyInt(int):
    """ My int class """

    def __eq__(self, value):
        """Override operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override operator with == behavior"""
        return self.real == value
