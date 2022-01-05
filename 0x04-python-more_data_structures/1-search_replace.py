#!/usr/bin/python3
""" a function that replaces all occurrences of an element """


def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    for i, j in enumerate(my_new_list):
        if j == search:
            my_new_list[i] = replace
    return my_new_list
