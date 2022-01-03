#!/usr/bin/python3
""" a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if my_list is None:
        return None
    max_integer = 0
    for i in my_list:
        if i >= max_integer:
            max_integer = i
    return max_integer
