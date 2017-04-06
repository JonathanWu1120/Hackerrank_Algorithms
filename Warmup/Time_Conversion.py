#!/bin/python3

import sys


time = input().strip()
time = time.split(":")
hr = int(time[0])
if time[2][2:] == "PM":
    if hr == 12:
        hr = 12
    else:
        hr += 12
if hr == 12 and time[2][2:] == "AM":
    hr = "00"
elif hr < 10:
    hr = "0"+str(hr)
print(str(hr)+":"+time[1]+":"+time[2][:2])