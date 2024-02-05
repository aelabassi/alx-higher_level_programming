#!/usr/bin/python3
"""
Function that checks is an object is a subclass of a class
"""


def is_same_class(obj: object, a_class: type) -> bool:
    """Returns True if object is a subclass of a_class
        Args:
            obj: (object): the object
            a_class: (class_) the class
        Returns
            True if object is a subclass of a_class
            False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
