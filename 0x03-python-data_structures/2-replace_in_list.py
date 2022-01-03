#!/usr/bin/python3
"""  a function that replaces an element of a list at a specific position"""


def replace_in_list(my_list, idx, element):
    """ replace an element of a list"""
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None
    my_list[idx] = element
    return my_list
