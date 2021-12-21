#!/usr/bin/python3
i = 0
while (i <= 8):
    j = i + 1
    while(j <= 9):
        if j == 9 and i == 8:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end="")
        j = j + 1
    i = i + 1
