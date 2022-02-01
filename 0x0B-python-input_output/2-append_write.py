#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8): """


def append_write(filename="", text=""):
    """ define a function"""
    with open(filename, "a+", encoding="utf-8") as f:
        numb_char = f.write(text)
    return numb_char
