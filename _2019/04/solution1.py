#! /usr/bin/env python3

INPUT = [347312, 805915]

def increasing_digits(num: int):
	digits = [int(d) for d in str(num)]

	for i in range(len(digits) - 1):
		if digits[i] > digits[i + 1]:
			return False

	return True

def two_adjacent(num: int):
	digits = [int(d) for d in str(num)]

	for i in range(len(digits) - 1):
		if digits[i] == digits[i + 1]:
			return True

	return False

answers = []

for num in range(INPUT[0], INPUT[1] + 1):
	if increasing_digits(num) and two_adjacent(num):
		answers.append(num)

print("There are {} answers".format(len(answers)))
