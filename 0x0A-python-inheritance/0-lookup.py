#!/usr/bin/python3
"""
This module provide a function that returns attributes
and methods of an object
"""


def lookup(obj):
    """ Returns a list of attributes
     and methods of an object
        Args:
            obj: (object) object or a class
        Returns:
            a list of all attributes and methods
    """
    attributes = [attr for attr in dir(obj)
                  if not callable(getattr(obj, attr, None))]
    methods = [m for m in dir(obj) if callable(getattr(obj, m, None))]
    all_ = attributes + methods
    return all_
