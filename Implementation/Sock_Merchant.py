#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d = set(c)
count = 0
for i in range(len(d)):
    x = d.pop()
    while c.count(x) >= 2:
        for i in range(2):
            c.remove(x)
        count += 1
print(count)
