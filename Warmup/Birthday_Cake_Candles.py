#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
highest = 0
for i in range(n):
    if height[i] > highest:
        highest = height[i]
print(height.count(highest))
