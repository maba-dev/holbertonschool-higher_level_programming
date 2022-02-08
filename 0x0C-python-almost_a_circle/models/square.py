#!/usr/bin/python3
""" the class Square that inherits from Rectangle: """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a super __init__"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ define a function __str__()"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.size
        ))

    @property
    def size(self):
        """ function getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """ function setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ function update"""
        i = 0
        list_args = ["id", "size", "height", "x", "y"]
        while (i < len(args)):
            setattr(self, list_args[i], args[i])
            i += 1
        if kwargs and kwargs != None:
            for key, value in kwargs.items():
                if key in list_args:
                    setattr(self, key, value)
