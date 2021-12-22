#!/usr/bin/python3
""" a function that creates a copy of the string, removing the position n"""


def remove_char_at(str, n):
    if n == 0:
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
