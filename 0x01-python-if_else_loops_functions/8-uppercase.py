#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 122:
            upper = chr(ord(i) - 32)
        else:
            upper = i
        print("{}".format(upper), end='')
    print()
