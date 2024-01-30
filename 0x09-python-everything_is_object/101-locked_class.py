#!/usr/bin/python3


class LockedClass:
    """ Class that prevent the user from dynamically
    creating new instance attributes
    """
    __slots__ = ["first_name"]
