#! /usr/bin/env python3

INPUT = [347312, 805915]

def increasing_digits(num: int):
	digits = [int(d) for d in str(num)]

	for i in range(len(digits) - 1):
		if digits[i] > digits[i + 1]:
			return False

	return True

def only_two_adjacent(num: int):
	digits = [int(d) for d in str(num)]

	i = 0
	while i < len(digits) - 1:
		c = 1

		for j in range(i + 1, len(digits)):
			if digits[j] == digits[i]:
				c = c + 1
			else:
				break

		if c == 2:
			return True

		i = i + c

	return False

answers = []

for num in range(INPUT[0], INPUT[1] + 1):
	if increasing_digits(num) and only_two_adjacent(num):
		answers.append(num)

print("There are {} answers".format(len(answers)))
