#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str1 = "and is less than 6 and not 0"
las_digit = number % 10
if number < 0:
    las_digit = number % -10
if las_digit > 5:
    print("{} {} is {} and is greater than 5".format(str, number, las_digit))
elif las_digit < 6 and las_digit != 0:
    print("{} {} is {} {}".format(str, number, las_digit, str1))
else:
    print("{} {} is {} and is 0".format(str, number, las_digit))
