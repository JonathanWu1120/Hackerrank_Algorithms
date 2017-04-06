#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if grade < 38:
        print(grade)
    else:
        if grade%5 == 0:
            bound = grade
        else:
            bound = (grade//5 + 1) *5
        if bound - grade < 3:
            print(bound)
        else:
            print(grade)