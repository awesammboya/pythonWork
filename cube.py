#!/usr/bin/python

# Find the cube  of the numbers
num = int(input("Enter the maximum number to cube: "))

# loop through from 1 till the max number entered 
for x in range( 1, num + 1) :
	# Print the cube of every number
	print("The cube of ",x, "is", (x * x * x))
