#!/usr/bin/python3
"""a function that prints the numbers from 1 to 100 separated by a space. """


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz ", end="")
        elif i % 3 == 0:
            print("fizz ", end="")
        elif i % 5 == 0:
            print("buzz ", end="")
        elif i == 100:
            print("fizz buzz")
        else:
            print("{:d} ".format(i), end="")
