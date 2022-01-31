#!/usr/bin/python3
"""A class MyList that inherits from list:"""


class MyList(list):
    """ define e class MyList"""
    def print_sorted(self):
        """ define a methode of the list"""
        print(sorted(self))
