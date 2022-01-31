#!/usr/bin/python3
"""a function that returns True if the object is an instance of"""


def is_kind_of_class(obj, a_class):
    """define a function"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
