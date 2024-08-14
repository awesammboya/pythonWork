#!/usr/bin/python

# Given two lists, convert them to a dictionary.
keys = ['Ten', 'Hundered', 'Thousand', 'Ten Thousand', 'Hundered Thousand', 'Million']
values =[10, 100, 1000, 10000, 100000, 1000000]

# Define an empty dictionary
res_dict = dict()

res_dict = dict(zip(keys, values))

print("Here's the dictionary from the two lists: \n", res_dict)
