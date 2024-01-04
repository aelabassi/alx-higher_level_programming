#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    n_args = len(args) - 1
    if n_args != 3:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        sys.exit(1)
    operator = args[2]
    if not(operator in  ("+", "-", "*", "/")):
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    result = 0
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
  