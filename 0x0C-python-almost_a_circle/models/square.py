#!/usr/bin/python3
""" the class Square that inherits from Rectangle: """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a super __init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ define a function __str__()"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.height
        ))
