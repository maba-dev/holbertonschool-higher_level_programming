#!/usr/bin/python3
"""  a function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """ define a function"""
    if type(obj) is a_class:
        return True
    else:
        return False
