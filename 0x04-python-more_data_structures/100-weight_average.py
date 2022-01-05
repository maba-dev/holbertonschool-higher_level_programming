#!/usr/bin/python3
""" a function that returns the weighted average of all integers tuple"""


def weight_average(my_list=[]):
    note = 0
    moy = 0
    if not my_list:
        return 0
    for (x, y) in my_list:
        note += y
        moy += y * x
    return moy / note
