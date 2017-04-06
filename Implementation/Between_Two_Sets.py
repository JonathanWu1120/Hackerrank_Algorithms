#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
c = []
d = set()
e = set()
for i in range(1,1+min(b)):
    if min(b)%i == 0 and i%min(a) == 0 and max(b)%i == 0 and i%max(a) == 0:
        c.append(i)

for element in c:
    if element%a[-1]==0:
        d.add(element)
for element in d:
    if b[0]%element==0:
        e.add(element)
print(len(e))
    