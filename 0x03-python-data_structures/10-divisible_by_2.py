#!/usr/bin/python3
"""  a function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    new_in_list = []
    for i in my_list:
        if i % 2 == 0:
            new_in_list.append(True)
        else:
            new_in_list.append(False)
    return new_in_list
