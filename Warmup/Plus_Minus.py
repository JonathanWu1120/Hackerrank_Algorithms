#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
p = 0
z = 0
ne = 0 
for i in range(n):
    if arr[i] < 0:
        ne += 1
    elif arr[i] > 0:
        p += 1
    else:
        z += 1
print(p/n)
print(ne/n)
print(z/n)
