#!/usr/bin/python3
"""
Append to the end of the file
"""


def append_write(filename="", text="") -> int:
    """Appends a string at the end of a text file
        Args:
            filename: (str) file
            text: (str) text
        Returns:
            number of characters
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
