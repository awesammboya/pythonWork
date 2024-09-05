#!/usr/bin/python

# This program finds all numbers which are divisible by 7 but are not a multiple of 5,
# Ranging between 2000 and 3200 (both included).
# The numbers obtained shall be printed in a comma-separated sequence on a single line.

listOfDivs = []
for num in range(2000, 3201):
	if num % 7 == 0 and num % 5 != 0:
		listOfDivs.append(str(num))

print(','.join(listOfDivs))

