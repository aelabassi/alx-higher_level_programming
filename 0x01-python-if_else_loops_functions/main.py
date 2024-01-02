#!/usr/bin/python3
uppercase = __import__("8-uppercase").uppercase
print_last_digit = __import__("9-print_last_digit").print_last_digit
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
uppercase("best")
uppercase("Best School 98 Battery street")
