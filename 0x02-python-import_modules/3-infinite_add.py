#!/usr/bin/python3
import sys


def add():
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    return result


print(add())
