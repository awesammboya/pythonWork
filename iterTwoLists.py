#!/usr/bin/python

# Given two python lists, iterate both lists simultaneously
# Display  items in list1 in original order and list2 in reverse order.

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]

for x, y in zip(list1, list2[::-1]):
	print(x, y)
