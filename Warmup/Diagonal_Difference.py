#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
left = 0
right = 0
ab = n
for x in range(n):
    left += a[x][x]
    right += a[x][ab-1]
    ab -= 1
print(abs(left-right))