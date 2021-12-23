#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        result = int(argv[1])
        for i in range(2, len(argv)):
            result += int(argv[i])
        print("{:d}".format(result))
