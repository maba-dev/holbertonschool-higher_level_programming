#!/usr/bin/python3
""" a function that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in my_list:
        if i == idx:
            del my_list[idx]
    return my_list
