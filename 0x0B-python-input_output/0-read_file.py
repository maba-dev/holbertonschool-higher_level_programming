#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ define a function"""
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)
    f.closed
