#!/usr/bin/python3
"""
load json file from an objet
"""
import json


def load_from_json_file(filename):
    """Create an object from a json file
        Args:
            filename:(str) file
        Returns:
            object
    """
    with open(filename) as file:
        return json.load(file)
