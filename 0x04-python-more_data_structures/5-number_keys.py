#!/usr/bin/python3
def number_keys(a_dictionary: dict):
    number_keys = 0
    for k in a_dictionary.keys():
        number_keys += 1
    return number_keys
