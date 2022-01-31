#!/usr/bin/python3
""" a class Square that inherits from Rectangle (9-rectangle.py):"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """define a class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
