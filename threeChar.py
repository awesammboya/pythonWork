#!/usr/bin/python
# This program  creates a new string  made of an input string's first, middle, and last character.

str1 = input("Enter your string: ")

print("Here's your string: ", str1)
# Get the first character.
res = str1[0]

# Get the middle index number and character
mi = int(len(str1)/2)
res = res + str1[mi]

# Get the last character and add it to the result
res = res + str1[(len(str1)-1)]

print("Your new string: ", res)
