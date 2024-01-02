#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str1 = "and is less than 6 and not 0"
las_digit = abs(number) % 10
if number < 0:
    if las_digit == 0:
        print(f"{str} {number:d} is {las_digit:d} and is 0")
    elif las_digit < 6 and las_digit != 0:
        print(f"{str} {number:d} is {-las_digit:d} {str1}")
else:
    if las_digit > 5:
        print(f"{str} {number:0} is {las_digit:d} and is greater than 5")
    elif las_digit == 0:
        print(f"{str} {number:0} is {las_digit:d} and is 0")
    elif las_digit < 6 and las_digit != 0:
        print(f"{str} {number:d} is {las_digit:d} {str1}")
