#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ define a function"""

    with open(filename, "w", encoding="utf-8") as f:
        numb_char = f.write(text)
    return numb_char
