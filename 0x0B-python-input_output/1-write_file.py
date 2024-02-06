#!/usr/bin/python3
"""
Write to file
"""


def write_file(filename="", text="") -> int:
    """Write to file and return the number of characters written
        Args:
            filename: (str) file
            text: (ste) text
        Returns:
            number of characters (int)
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
