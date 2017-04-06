#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
tracker = 0
#loop to go through every item in a
for i in range(len(a)):
    #loop to go through the other terms
    for j in range(i+1,len(a)):
        #
        if (a[i]+a[j]) % k == 0:
            tracker += 1
print(tracker)
