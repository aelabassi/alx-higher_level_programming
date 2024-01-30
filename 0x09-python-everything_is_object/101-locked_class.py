#!/usr/bin/python3
""" This module have a class that reduce memory usage by
preventing the user from accessing the attributes"""


class LockedClass:
    """ Class that prevent the user from dynamically
    creating new instance attributes
    """
    __slots__ = ["first_name"]
