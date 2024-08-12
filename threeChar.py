#!/usr/bin/python
# This program  creates a new string of an input string's first, middle, and last characters.

str1 = input("Enter your string: ")

print("Here's the string entered: ", str1)
# Get the first character of the string.
res = str1[0]

# Get the middle index number and character
# First, calculate the index of the middle character by dividing the length of the string into 2.
mi = int(len(str1)/2)

# Now, add the middle character to the first character of the string.
res = res + str1[mi]

# Get the last character and add it to the result
res = res + str1[(len(str1)-1)]

print("Your new string is: ", res)
