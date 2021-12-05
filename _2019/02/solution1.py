#! /usr/bin/env python3

def f_add(code: list, pos: int):
	add_1 = code[pos + 1]
	add_2 = code[pos + 2]
	add_3 = code[pos + 3]

	n_1 = code[add_1]
	n_2 = code[add_2]
	n_3 = n_1 + n_2

	code[add_3] = n_3

	return 0

def f_mul(code: list, pos: int):
	add_1 = code[pos + 1]
	add_2 = code[pos + 2]
	add_3 = code[pos + 3]

	n_1 = code[add_1]
	n_2 = code[add_2]
	n_3 = n_1 * n_2

	code[add_3] = n_3

	return 0

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

		# Check that we have that operation.. =)
		if f is None:
			raise KeyError
			break

		res = f(code, pos)

		if res is not None and res == -1:
			break

		pos = pos + 4

# code = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50] # res -> [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

code = [int(a) for a in open("input.txt").read().split(",")]

code[1] = 12
code[2] = 2

intcode(code)

print("Solution is {}".format(code[0]))
