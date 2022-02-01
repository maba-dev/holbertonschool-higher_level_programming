#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8) and returns the number of characters added: """

def append_write(filename="", text=""):
    with open(filename, "a+", encoding="utf-8") as f:
        numb_char = f.write(text)
    return numb_char