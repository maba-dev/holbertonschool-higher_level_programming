#!/usr/bin/python3
""" a function that prints a string in uppercase followed by a new line."""


def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 97 and i <= 122:
            i -= 32
        print("{:c}".format(i), end='')
    print()