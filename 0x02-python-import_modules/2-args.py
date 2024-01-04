#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    n_args = len(args) - 1
    if n_args == 1:
        print("{} argument:".format(n_args))
        print("{}: {}".format(n_args, args[n_args]))
    elif n_args == 0:
        print("{} arguments.".format(n_args))
    else:
        print("{} arguments:".format(n_args))
        for arg in range(1, len(args)):
            print("{}: {}".format(arg, args[arg]))
