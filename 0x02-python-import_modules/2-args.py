#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:\n1: {:s}".format(argv[1]))
        else:
            j = 1
            print("{:d} arguments:".format(len(argv) - 1))
            for j in range(1, len(argv)):
                print("{:d}: {:s}".format(j, argv[j]))
