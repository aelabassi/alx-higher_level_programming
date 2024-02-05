#!/usr/bin/python3
"""
This function checks for the instance and subclass of an object
"""


def is_kind_of_class(obj: object, a_class: type) -> bool:
    """obj is instance of a_class or subclass
        Args:
            obj: (object) the object
            a_class: (type) the type
        Returns:
            True if the object is an instance
            or subclass, False otherwise
    """
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    return False
