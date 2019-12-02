#! /usr/bin/env python3

import math

def fuel_for_module(mass: float):
	return math.floor(mass / 3) - 2

def fuel_for_modules(modules: list):
	return [fuel_for_module(mass) for mass in modules]

def read_modules(filename: str):
	modules = []

	with open(filename, "r") as f:
		for line in f.readlines():
			mass = float(line)
			modules.append(mass)

	return modules

modules = read_modules("./input.txt")

print("Loaded mass for {} modules".format(len(modules)))

fuels = fuel_for_modules(modules)

print("Calculated fuel for each module")

total_fuel = sum(fuels)

print("Total sum of fuel is {}".format(total_fuel))
