#!/bin/python3

def out_of_constraint(number):
    #'Yes' if fruit == 'Apple' else 'No'
    if number not in range(0,10**10+1):
        print("Out of range")
        exit()

if __name__ == '__main__':

    a = int(input())
    out_of_constraint(a)
    b = int(input())
    out_of_constraint(b)
   
    sum = a+b
    sub = a-b
    prod = a*b

    print(f"Sum: {a}+{b}={sum}")
    print(f"Sub: {a}-{b}={sub}")
    print(f"Prod: {a}*{b}={prod}")