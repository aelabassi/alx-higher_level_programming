#!/usr/bin/python3
"""
Adds argument to a python list and save them in json file
"""
import sys

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
