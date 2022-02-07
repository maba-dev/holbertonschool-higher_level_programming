#!/usr/bin/python3
"""the class Rectangle that inherits from Base: """
from models.base import Base


class Rectangle(Base):
    """ define a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter function"""
        return self.__width

    @width.setter
    def width(self, width):
        """ setter function"""
        if type(width) is not int:
            raise TypeError("width must be integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter function"""
        return self.__height

    @height.setter
    def height(self, height):
        """ getter function"""
        if type(height) is not int:
            raise TypeError("height must be integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter function"""
        return self.__x

    @x.setter
    def x(self, x):
        """ getter function"""
        if type(x) is not int:
            raise TypeError("x must be integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter function"""
        return self.__y

    @y.setter
    def y(self, y):
        """ getter function"""
        if type(y) is not int:
            raise TypeError("y must be integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ define a function"""
        return self.height * self.width

    def display(self):
        """ define a function"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ define a function"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height))
