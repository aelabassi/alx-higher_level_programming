#!/usr/bin/env python3
"""algorithm to find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find the peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
