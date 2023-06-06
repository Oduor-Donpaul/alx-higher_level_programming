#!/usr/bin/python3
def remove_char_at(str, n):
    dest = ''
    for i in range(len(str)):
        if i != n:
            dest += str[i]
    return dest
