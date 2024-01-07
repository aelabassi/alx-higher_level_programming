#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        is_multiple_of_2 = []
        for i in my_list:
            if i % 2 == 0:
                is_multiple_of_2.append(True)
            else:
                is_multiple_of_2.append(False)
    return is_multiple_of_2
