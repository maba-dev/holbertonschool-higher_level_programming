#!/usr/bin/python3
""" a function that replaces an element in a list at a specific position """


def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_new_in_list = my_list.copy()
    my_new_in_list[idx] = element
    return my_new_in_list
