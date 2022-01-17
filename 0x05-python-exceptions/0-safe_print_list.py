#!/usr/bin/python3
""" a function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except IndexError:
            break
    print()
    return i
