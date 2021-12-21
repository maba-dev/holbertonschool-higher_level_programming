#!/usr/bin/python3
i = 0
while (i <= 9):
    j = 0
    while(j <= 9):
        if (i == 9 and j == 9):
            print("99")
        else:
            print("{:d}{:d}, ".format(i, j), end="")
        j = j+1
    i = i + 1
