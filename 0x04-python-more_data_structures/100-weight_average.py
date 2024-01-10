#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        average = 0
        sum_norm = 0
        for x in my_list:
            sum_norm += x[1]
        for x in my_list:
            average += x[0] * x[1] / sum_norm
        return average
