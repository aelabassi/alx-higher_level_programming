#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        diff_ = 0
    else:
        diff_ = 32
    print("{}".format(chr(i - diff_)), end='')
