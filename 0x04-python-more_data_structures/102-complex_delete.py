#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value):
    key_to_delete = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_to_delete.append(key)
    for key in key_to_delete:
        del a_dictionary[key]
    return a_dictionary
