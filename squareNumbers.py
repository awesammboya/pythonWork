#!/usr/bin/python
# Given a number in a list, find the square of each number element in the given list.
numbers = [2, 34, 47, 91, 89, 123, 217, 313, 69, 297]
res = [ x * x for x in numbers ]
print("The numbers given in a list: ", numbers,"\n")
print("The squares of the numbers given ", res)
