#!/usr/bin/python3
""" a class MyInt that inherits from int:"""


class MyInt(int):
    """ define a class"""
    def __eq__(self, other):
        return super() == other

    def __ne__(self, other):
        return not self == other
