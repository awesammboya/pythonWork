#!/usr/bin/python

# A prime number is a number that cannot be made by multiplying other whole numbers.
start = int(input("What is the start number: "))
end = int(input("What is the end number: "))

print("Prime numbers between ", start, "and ", end, "are: ")

for num in range(start, end + 1):
	# all prime #s are greater than 1.
	# if number is less than or equal to 1, it's not prime
	if num > 1:
		for i in range(2, num):
			# check for factors
			if (num % i) == 0:
				# not a prime # so break the inner loop and try next number
				break
		else:
			print(num)

