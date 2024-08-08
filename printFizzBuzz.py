#!/usr/bin/python

for i in range(1, 51):
    # If the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    # If the current number is divisible only by 3
    elif i % 3 == 0:
        print("Fizz")
        continue
    # Check if the current number is divisible only by 5
    elif i % 5 == 0:
        print("Buzz")
        continue
    # Else, print the number itself
    print(i)
