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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)



    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs
        to a file
        """
        file = cls.__name__ + ".json"
        contents = []
        if list_objs is not None:
            for item_ in list_objs:
                item_dic = item_.to_dictionary()
                item_dec = json.loads(cls.to_json_string(item_dic))
                contents.append(item_dec)
        with open(file, "w") as f:
            json.dump(contents, f)
