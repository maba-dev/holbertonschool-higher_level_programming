#!/usr/bin/python3
"""  a function that prints a square with the character #."""


def print_square(size):
    """ define a function that prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
