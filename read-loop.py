#!/bin/python3

def check_constraint(num):
    if num not in range(1,20+1):
        exit()

if __name__ == '__main__':
    n = int(input())
    check_constraint(n)

    for num in range(n+1):
        if num >= 0 and num < n:
                print(num**2)
    
    #print(*[num**2 for num in range(n)], sep='\n') #is the same
