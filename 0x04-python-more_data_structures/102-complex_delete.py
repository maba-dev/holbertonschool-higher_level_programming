#!/usr/bin/python3
""" a function that deletes keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
