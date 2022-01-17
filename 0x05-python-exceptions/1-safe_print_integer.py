#!/usr/bin/python3
""" a function that prints an integer with "{:d}".format()."""


def safe_print_integer(value):
    try:
        print("{:d}\n".format(value))
        return True
    except:
        return False
    