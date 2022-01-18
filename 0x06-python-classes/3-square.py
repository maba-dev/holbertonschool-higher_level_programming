#!/usr/bin/python3
"""  a class Square that defines a square by: (based on 2-square.py) """


class Square:
    """Define Class"""
    def __init__(self, size=0):
        """ Define class constructor"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Define method area"""
        return self.__size * self.__size
