#!/usr/bin/python3
"""
This function checks if an object is an instance of a class
that inherited (directly or indirectly) from
the specified class
"""


def inherits_from(obj: object, a_class: type) -> bool:
    """Returns True if an abject is an instance of
    class that inherited from specified class
        Args:
            obj: (object) the object
            a_class: (type) the class type
        Returns:
            True of object is an instance of a_class
            False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
