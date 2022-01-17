#!/usr/bin/python3
from sys import stderr
""" a function that prints an integer."""

def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=stderr)
        return False