#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if a_dictionary is None:
        return None
    else:
        max_value = 0
        max_key = ""
        for k, v in a_dictionary.items():
            if v > max_value:
                max_value = v
                max_key = k
        return max_key
