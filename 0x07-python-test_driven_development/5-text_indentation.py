#!/usr/bin/python3
""" a function that prints a text with 2 new lines after: ., ? and :"""


def text_indentation(text):
    """ a function that prints text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    for i in range(0, len(text)):
        string += text[i]
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            string += "\n\n"
    string_last = ""
    for j in range(0, len(string)):
        if (string[j - 1] == '\n') and string[j] == ' ':
            continue
        else:
            string_last += string[j]
    print("{:s}".format(string_last), end="")
