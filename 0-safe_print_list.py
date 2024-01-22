#!/usr/bin/bash
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[:x])
        nb_print = 0
        for i in my_list[:x]:
            nb_print += 1
    except IndexError:
        pass
    else:
        return nb_print

