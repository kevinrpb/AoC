#! /usr/bin/env python3

def f_add(code: list, pos: int):
	add_1 = code[pos + 1]
	add_2 = code[pos + 2]
	add_3 = code[pos + 3]

	n_1 = code[add_1]
	n_2 = code[add_2]
	n_3 = n_1 + n_2

	code[add_3] = n_3

def f_mul(code: list, pos: int):
	add_1 = code[pos + 1]
	add_2 = code[pos + 2]
	add_3 = code[pos + 3]

	n_1 = code[add_1]
	n_2 = code[add_2]
	n_3 = n_1 * n_2

	code[add_3] = n_3

def f_hal(code: list, pos: int):
	return -1

OP_ADD = 1
OP_MUL = 2
OP_HAL = 99

OP = {
	OP_ADD: f_add,
	OP_MUL: f_mul,
	OP_HAL: f_hal
}

def intcode(code: list):
	pos = 0

	while pos < len(code):
		op = code[pos]
		f = OP[op]

		if f is None:
			raise KeyError
			break

		res = f(code, pos)

		if res is not None and res == -1:
			break

		pos = pos + 4

def find(initial_code: list, GOAL: int):
	for n in range(0, 100):
		for v in range(0, 100):
			code = list(initial_code)
			code[1] = n
			code[2] = v

			intcode(code)

			res = code[0]

			if res == GOAL:
				return (n, v)

	return (None, None)

initial_code = [int(a) for a in open("input.txt").read().split(",")]

GOAL = 19690720

noun, verb = find(initial_code, GOAL)

print("Noun is\t{}\nVerb is\t{}".format(noun, verb))
print("100 * noun + verb is {}".format(100 * noun + verb))
