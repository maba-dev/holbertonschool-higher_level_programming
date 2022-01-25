#!/usr/bin/python3
""" a function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    for i in range(0, len(text)):
        string += text[i]
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            string += "\n \n"
    print("{:s}\n".format(string))
