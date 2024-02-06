#!/usr/bin/python3

add_item = __import__('7-add_item').add_item

try:
    add_item("add_item.json")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
