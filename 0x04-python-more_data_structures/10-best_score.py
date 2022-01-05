#!/usr/bin/python3
""" a function that returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    return (max(a_dictionary, key=a_dictionary.get))
