#!/usr/bin/python3
"""
This module have a function that print full name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints the full name
    Args:
        first_name (str): frist name
        last_name (str): last name
    Return:
        full_name (str): first_name + last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
