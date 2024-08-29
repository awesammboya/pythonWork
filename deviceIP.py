#!/usr/bin/python

# Import os library
import os

# Leverage system() function from the os library to execute a bash script that runs ifconfig command
# Save the output in ifconfig.txt
os.system("ifconfig > ifconfig.txt")

# Use with statement and open() to read the ifconfig.txt in read mode
# into a variable named if_file
with open("ifconfig.txt", 'r') as if_file:
    # use for loop to iterate through the lines, treating each line as separate list
    for line in if_file.readlines():
        if 'broadcast' in line: # find the line with 'broadcast'
            split_line = line.split() # do a split into that line
            # inet 172.17.0.13  netmask 255.255.0.0  broadcast 172.17.255.255
            # the IP is in index 1.
            # print the IP using the f-string; terminate the iteration using break statement.
            print(f"Your IP is: {split_line[1]}")
            break
