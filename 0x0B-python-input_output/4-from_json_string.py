#!/usr/bin/python3
"""
json to python object
"""
import json


def from_json_string(my_str):
    """Returns a python object
        Args:
            my_str: (str) json string
        Returns:
            python object
    """
    return json.loads(my_str)
