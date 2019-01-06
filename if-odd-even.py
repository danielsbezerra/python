#!/bin/python3

N = int(input())
R = range(0,101)

if N in R:
    if N%2 != 0: #odd
        print("Weird")
    elif N in range(2,5):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    elif N > 20:
        print("Not Weird")
else:
    print(f"{N} out of range(0,101)")