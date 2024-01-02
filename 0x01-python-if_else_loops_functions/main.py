#!/usr/bin/python3
uppercase = __import__("8-uppercase").uppercase
print_last_digit = __import__("9-print_last_digit").print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
uppercase("best")
uppercase("Best School 98 Battery street")
