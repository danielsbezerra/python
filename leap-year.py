#!/bin/python3

def check_constraint(num):
    if num not in range(1900,10**5):
        exit()

def is_leap(year):
    leap = False
    
    if year %4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
    return leap
    # return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())

print(is_leap(year))