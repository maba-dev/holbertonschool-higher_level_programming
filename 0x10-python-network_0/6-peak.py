#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    size = len(list_of_integers)
    if (size == 0) :
      return None
    list_of_integers.sort()
    result = list_of_integers[-1]
    return result
