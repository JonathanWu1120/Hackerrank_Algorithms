#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
def make_lis(a,b,c,d,e):
    lis = []
    lis.append(a)
    lis.append(b)
    lis.append(c)
    lis.append(d)
    lis.append(e)
    return lis
def big(a,b):
    if a > b:
        return a
    else:
        return b
def small(a,b):
    if a > b:
        return b
    else:
        return a
def mi():
    lis = make_lis(a,b,c,d,e)
    lis.remove(small(a,small(b,small(c,small(d,e)))))
    summ = 0
    for i in range(len(lis)):
        summ += lis[i]
    return summ
def bi():
    lis = make_lis(a,b,c,d,e)
    lis.remove(big(a,big(b,big(c,big(d,e)))))
    summ = 0
    for i in range(len(lis)):
        summ += lis[i]
    return summ
    
print(bi(),mi())