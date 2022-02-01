#!/usr/bin/python3
"""a class Student that defines a student by: """


class Student:
    """ deefine class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dict = {}
        for i in attrs:
            if isinstance(i, str) and hasattr(self, i):
                dict[i] = getattr(self, i)
        return dict
