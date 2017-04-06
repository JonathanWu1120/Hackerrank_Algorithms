#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
def count_num(lis,number):
    return lis.count(number)
arr = []
for i in range(5):
    arr.append(types.count(i+1))
index = 0
mv = 0
for i,x in enumerate(arr):
    if x > mv:
        index = i
        mv = x
print(index+1)

