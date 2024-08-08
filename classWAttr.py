#!/usr/bin/python

# This programs create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage

Tesla = Vehicle(240, 18)
print(Tesla.max_speed, Tesla.mileage)
