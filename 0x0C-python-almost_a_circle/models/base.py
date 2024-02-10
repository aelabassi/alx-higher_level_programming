#!/usr/bin/python3
"""
Base model
"""
import json


class Base:
    """ Class Base """
    __nb__objects = 0

    def __init__(self, id=None):
        """Init a new Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json format"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
