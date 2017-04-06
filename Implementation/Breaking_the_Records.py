#!/bin/python3

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
# your code goes here
lowest = score[0]
highest = score[0]
high_tracker = 0
low_tracker = 0
for i in score:
    if i > highest:
        highest = i
        high_tracker += 1
    if i < lowest:
        lowest = i
        low_tracker += 1
print(high_tracker,low_tracker)
