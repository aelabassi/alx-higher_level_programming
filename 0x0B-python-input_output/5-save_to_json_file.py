#!/usr/bin/python3
"""
Save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to text file using json representation
        Args:
            my_obj: (object) object
            filename: (str) fil
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
