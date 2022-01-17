#!/usr/bin/python3
"""a function that prints the first x elements of a list and only integers. """


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            continue
    print()
    return(i + 1)
