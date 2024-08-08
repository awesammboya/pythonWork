#!/usr/bin/python
num1, num2 = 0, 1

fibvalues = int(input("How many fibonacci numbers do you want: "))

print("Fibonacci sequence: ")

for i in range(fibvalues):
	# print next number of series
	print(num1, end = " ")
	# add last two numbers to get the next number
	res = num1 + num2
	# update values
	num1 = num2
	num2 = res
print()
