#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict):
    my_list = [k for k in a_dictionary.keys()]
    my_list = sorted(my_list)
    for i in range(len(my_list)):
        print("{}: {}".format(my_list[i], a_dictionary[my_list[i]]))
