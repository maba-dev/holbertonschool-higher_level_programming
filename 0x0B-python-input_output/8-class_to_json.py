#!/usr/bin/python3
"""function that returns the dictionary description with simple data struct"""


def class_to_json(obj):
    """ define a function"""
    return obj.__dict__
