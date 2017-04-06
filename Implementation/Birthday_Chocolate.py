#!/bin/python3

import sys

def getWays(s, d, m):
    total = 0
    for c in range(len(s)-m+1):
        accum = 0
        if accum < d:
            for i in range(m):
                accum += s[i+c]
        if accum == d:
            total += 1
        accum = 0
    return total

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)