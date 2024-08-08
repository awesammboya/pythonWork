#!/usr/bin/python
# Check if the entered string is a palindrome.
def isPalindrome(string):
	if string.lower() == string[::-1].lower():
		return "The string " + string + " is palindrome!"
	else:
		return "The string "+ string + " is NOT a palindrome"
# Enter an input string
string = input("Enter a string: ")
print(isPalindrome(string))

