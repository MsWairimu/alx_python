#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if (i != 8 or j != 9):
            end_char = ", "
        elif(i == 8 and j == 9):
            end_char = "\n"
        print("{:d}{:d}".format(i,j), end=end_char)
