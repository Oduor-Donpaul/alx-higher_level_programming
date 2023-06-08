#!/usr/bin/python3
import sys
if __name__ = "__main__"
    args = len(sys.argv) - 1
    print("{} argument.".format(args) if args == 1
          else "{} arguments:".format(args))
    if args > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
