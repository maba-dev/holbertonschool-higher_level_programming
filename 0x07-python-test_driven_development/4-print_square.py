#!/usr/bin/python3
"""  a function that prints a square with the character #."""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            if j == size - 1:
                print("\n")
            j += 1
        i += 1
