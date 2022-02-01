#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a list of lists of integers"""


def pascal_triangle(n):
    """ define a function"""
    list = []
    if n <= 0:
        return list
    for _ in range(n):
        row = [1]
        if list:
            last_row = list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        list.append(row)
    return list
