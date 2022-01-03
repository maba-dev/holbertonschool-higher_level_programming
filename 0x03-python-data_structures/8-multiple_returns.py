#!/usr/bin/python3
"""  a function that returns a tuple"""


def multiple_returns(sentence):
    if len(sentence) < 0:
        return None
    return (len(sentence), sentence[0])
