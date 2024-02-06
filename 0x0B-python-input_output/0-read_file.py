#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Reads a file,and prints it ro stdout
        Args:
            filename: (str) file
    """
    with open(filename, "r") as file:
        text = file.read()
        print(text)
