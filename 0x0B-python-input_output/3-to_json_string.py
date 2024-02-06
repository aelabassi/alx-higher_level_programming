#!/usr/bin/python3
"""
Sterializarion with json
"""
import json


def to_json_string(my_obj: object):
    """Returns a serialized string
        Args:
            my_obj: (object)
        Returns:
            jsonyfied object
    """
    return json.dumps(my_obj)
