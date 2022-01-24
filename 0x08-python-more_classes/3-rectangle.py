#!/usr/bin/python3
""" a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """ define a rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return (string)
        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                string += "#"
                j += 1
            string += "\n"
            i += 1
        return (string)

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (2 * (self.__height + self.__width))
