#!/bin/python3

import numpy
n, m = map(int, input().split())
my_array = numpy.array([input().split() for _ in range(n)], int)

sum=numpy.sum(my_array, axis=0)
print(sum)

prod=numpy.prod(sum)
print(prod)

# import numpy
# def compute():
#     dim = input().split()
#     for i in range(len(dim)):
#         dim[i] = int(dim[i])

#     arr = []
#     for i in range(dim[0]):
#         ele = numpy.array(input().split() , int)
#         arr.append(ele)
#     arr = numpy.array(arr)

#     print(numpy.prod(numpy.sum(arr , axis = 0)))
# compute()