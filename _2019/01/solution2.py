#! /usr/bin/env python3

import math

def fuel_for_module(mass):
	def calc_fuel(mass):
		return math.floor(mass / 3) - 2

	total = 0
	fuel = calc_fuel(mass)

	while fuel > 0:
		total = total + fuel
		fuel = calc_fuel(fuel)

	return total

def read_input(filename):
	lines = open(filename).readlines()

	modules = [int(line) for line in lines]

	return modules

modules = read_input("input.txt")

fuel = [fuel_for_module(module) for module in modules]

total_fuel = sum(fuel)

print("Total sum of fuel is {}".format(total_fuel))
