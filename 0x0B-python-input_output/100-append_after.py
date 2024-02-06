#!/usr/bin/python
"""
Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text ro a file, after each line containing a specific string
    Args:
        filename: (str) file
        search_string: (str) search string
        new_string: (str) string to insert

    Returns:

    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        index = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(index + 1, new_string)
            index += 1
        file.seek(0)
        file.write("".join(lines))
