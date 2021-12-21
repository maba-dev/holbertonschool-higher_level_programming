#!/usr/bin/python3
"""a function that prints the last digit of a number."""


def print_last_digit(number):
    """print the last digit of a number"""
    i = abs(number) % 10
    print("{:d}".format(i), end="")
    return (i)
