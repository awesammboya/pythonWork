#!/usr/bin/python
'''
Write a program that prints the first half values in one line
and the second half  values in a second line.
'''
tuple = (2002,2009,2016,2023,2037,2044,2051,2058,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2471,2478,2492,2499,2506,2513,2527,2534,2541)
midpoint = int(len(tuple)/2)
tp1 = tuple[:midpoint]
tp2 = tuple[midpoint:]

print(tp1)
print(tp2)

