#!/usr/bin/python3
" a function that divides 2 integers and prints the result."


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result
