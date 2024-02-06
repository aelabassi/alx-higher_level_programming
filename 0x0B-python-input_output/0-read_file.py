#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Reads a file,and prints it ro stdout
        Args:
            filename: (str) file
    """
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
