#!/usr/bin/python
num1, num2 = 0, 1
try:
	fibvalue = int(input("How many fibonacci numbers do you want: "))
except ValueError:
	print("Invalid input. Please enter a valid number.")
except KeyboardInterrupt:
	print("\nOperation cancelled by the user.")

print("Fibonacci sequence: ")

for i in range(fibvalue):
	# print next number of series
	print(num1, end = " ")
	# add last two numbers to get the next number
	res = num1 + num2
	# update values
	num1 = num2
	num2 = res
print()
