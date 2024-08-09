#!/usr/bin/python
# Find the Maximum number in a list.
givenList = [170, 23, 20, 34, 123, 34, 45, 78, 90, 45, 91, 23, 128, 4, 3, 222, 890, 389, 22]

# Set the max number to be the element at index 0
maxNum = givenList[0]
sum = 0
# Loop through the list
for num in givenList:
	if maxNum < num:
		maxNum = num
	sum = sum + num
# print the value of the max
print("The maximum number in the list is ",maxNum, "and the sum is ", sum)
