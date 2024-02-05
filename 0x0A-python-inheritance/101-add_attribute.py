#!/usr/bin/python3
"""
Function that adds an attribute to an object
"""


def add_attribute(obj: object, attr, value):
    """Sets an attribute
        Args:
            obj: (object)
            attr: (str) name of the attribute
            value (Any) value to set
        Raises:
            TypeError: if the object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
