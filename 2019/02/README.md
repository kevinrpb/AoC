> [Back Home](/)   &#124;&#124;   [Back to 2019](/2019/)

# AoC 2019 - December 2

## Problem I

On the way to your gravity assist around the Moon, your ship computer beeps angrily about a "1202 program alarm". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have escaped. "That computer ran Intcode programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

For example, suppose you have the following program:

	1,9,10,3,2,3,11,0,99,30,40,50

For the purposes of illustration, here is the same program split into multiple lines:

	1,9,10,3,
	2,3,11,0,
	99,
	30,40,50

The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent the first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of the output (3). To handle this opcode, you first need to get the values at the input positions: position 9 contains 30, and position 10 contains 40. Add these numbers together to get 70. Then, store this value at the output position; here, the output position (3) is at position 3, so it overwrites itself. Afterward, the program looks like this:

	1,9,10,70,
	2,3,11,0,
	99,
	30,40,50

Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, but it multiplies instead of adding. The inputs are at positions 3 and 11; these positions contain 70 and 50 respectively. Multiplying these produces 3500; this is stored at position 0:

	3500,9,10,70,
	2,3,11,0,
	99,
	30,40,50

Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

* `1,0,0,0,99` becomes `2,0,0,0,99` (1 + 1 = 2).
* `2,3,0,3,99` becomes `2,3,0,6,99` (3 * 2 = 6).
* `2,4,4,5,99,0` becomes `2,4,4,5,99,9801` (99 * 99 = 9801).
* `1,1,1,4,99,5,6,0,99` becomes `30,1,1,4,2,5,6,0,99`.

Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

To begin, [get your puzzle input](input.txt).

### Solution

> [Source code here](solution1.py)

Firstly, we are going to define three methods that will execute each of the different operations. These will receive a list with the intcode and the position where the opcode was found. Using that the methods will make the calculations and return `0` if it was successful or `-1` if the program should stop (halt instruction):

```python
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
```

To be able to access these functions in an easier way, we store them in a dict keyed by opcodes:

```python
OP_ADD = 1
OP_MUL = 2
OP_HAL = 99

OP = {
	OP_ADD: f_add,
	OP_MUL: f_mul,
	OP_HAL: f_hal
}
```

Now we are ready to code the core of the problem: the intcode _interpreter_.

We will be traveling the intcode array secuentially. To do so we store the current position in a variable (our pointer) and loop while that position is within bounds. Each loop we update the pointer by `4`.

```python
def intcode(code: list):
	pos = 0

	while pos < len(code):
		# Update position
		pos = pos + 4
```

Next we will extract the opcode from the array and use it to retrieve the method we need to execute from the dictionary.

```python
def intcode(code: list):
	pos = 0

	while pos < len(code):
		# Get opcode and function
		op = code[pos]
		f = OP[op]

		# Update position
		pos = pos + 4
```

Once we obtain the function, we can call it and check the result for the halt operation.

```python
def intcode(code: list):
	pos = 0

	while pos < len(code):
		# Get opcode and function
		op = code[pos]
		f = OP[op]

		# Call method
		res = f(code, pos)

		# Check if halt
		if res == -1:
			break

		# Update position
		pos = pos + 4
```

Now we are all set to find the solution (remember to change the second and third items!).

```python
# Read input and cast into array of ints
code = [int(a) for a in open("input.txt").read().split(",")]

# Set initial state
code[1] = 12
code[2] = 2

# Do intcode
intcode(code)

# Retrieve result
print("Solution is {}".format(code[0]))
```

<details>
	<summary>Solution</summary>

	Solution is 3654868
</details>

## Problem II

"Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll probably use it again. Real Intcode computers support many more features than your new one, but we'll let you know what they are as you need them."

"However, your current priority should be to complete your gravity assist around the Moon. For this mission to succeed, we should settle on some terminology for the parts you've already built."

Intcode programs are given as a list of integers; these values are used as the initial state for the computer's memory. When you run an Intcode program, make sure to start by initializing memory to the program's values. A position in memory is called an address (for example, the first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode, if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction finishes, the instruction pointer increases by the number of values in the instruction; until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions. (The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

Although it hasn't changed, you can still [get your puzzle input](input.txt).

### Solution

> [Source code here](solution2.py)

Once we have our intcode interpreter working, attacking the second part is arguably manageable. You guessed it: we are going to brute-force it.

```python
def find(initial_code: list, GOAL: int):
	# Iterate for values of noun and verb
	for n in range(0, 100):
		for v in range(0, 100):
			# Make a copy of the list and set initial state
			code = list(initial_code)
			code[1] = n
			code[2] = v

			# Do intcode and get result
			intcode(code)
			res = code[0]

			# If this is the goal, return int
			if res == GOAL:
				return (n, v)

	# We couldn't get to the goal...
	return (None, None)
```

Now to find our solution:

```python
initial_code = [int(a) for a in open("input.txt").read().split(",")]

GOAL = 19690720

noun, verb = find(initial_code, GOAL)

print("Noun is\t{}\nVerb is\t{}".format(noun, verb))
print("100 * noun + verb is {}".format(100 * noun + verb))
```

<details>
	<summary>Solution</summary>

	Noun is 70
	Verb is 14
	100 * noun + verb is 7014
</details>
