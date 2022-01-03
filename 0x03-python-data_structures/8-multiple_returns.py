#!/usr/bin/python3
"""  a function that returns a tuple"""


def multiple_returns(sentence):
    if len(sentence) <= 0:
        i = None
    else:
        i = sentence[0]
    return (len(sentence), i)
