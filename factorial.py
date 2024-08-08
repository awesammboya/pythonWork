#!/usr/bin/python
# This program prints back a factorial of a given number.
# For example 3! = 3 * 2 * 1 = 6

num = int(input("What number do you need a factorial for: "))
factorial = 1

if num < 0:
	print("Factorial does not exist for a negative numbers!")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	# Run loop num times.
	for i in range(1, num + 1):
		# multiply factorial by current number
		factorial = factorial * i
	print("The factorial of ", num, "is ", factorial)
