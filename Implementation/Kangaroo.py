#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
while (x1 != x2) and x1 < 100000000 and x2 < 100000000:
    if x2 > x1 and v2 > v1:
        break
    elif v2 == v1 and x2 != x1:
        break
    else:
        x1 += v1
        x2 += v2
if x1 == x2:
    print("YES")
else:
    print("NO")