#!/usr/bin/python

def get_middle_three_chars(str1):
	print("Original string is: ", str1)

	# first get the middle index number
	mi = int( len(str1) / 2 )

	# use string slicing to get result characters
	res = str1[mi - 1: mi + 2]
	print("Middle three chars are: ", res)

get_middle_three_chars("JHonDipPEta")
get_middle_three_chars("JaSonAy")