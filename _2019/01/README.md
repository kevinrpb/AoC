> [Back Home](/)   &#124;&#124;   [Back to 2019](/2019/)

# AoC 2019 - December 1

## Problem I

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

* For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
* For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
* For a mass of 1969, the fuel required is 654.
* For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

To begin, [get your puzzle input](input.txt).

### Solution

> [Source code here](solution1.py)

First of all, we need to either copy the input into our code or, alternatively, read it from th file:

```python
def read_input(filename):
	# read each line
	lines = open(filename).readlines()

	# cast all numbers from str to int
	modules = [int(line) for line in lines]

	return modules
```

We also need a way to calc the fuel for a given modules/mass. This is (almost) trivial:

```python
import math

def fuel_for_module(mass):
	return math.floor(mass / 3) - 2
```

With these two methods, we can find the answer:

```python
modules = read_input("input.txt")

fuel = [fuel_for_module(module) for module in modules]

total_fuel = sum(fuel)

print("Total sum of fuel is {}".format(total_fuel))
```

<details>
	<summary>Solution</summary>

	Total sum of fuel is 3374289
</details>

## Problem II

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

Although it hasn't changed, you can still [get your puzzle input](input.txt).

### Solution

> [Source code here](solution2.py)

In order to add for the new rules, we need to modify our `fuel_for_module()` method. We will start by adding an inner function that calcs the fuel for a given mass. Part I would look like this, then:

```python
def fuel_for_module(mass):
	def calc_fuel(mass):
		return math.floor(mass / 3) - 2

	return calc_fuel(mass)
```

Now we need to account for the extra mass of the fuel, to do so we will keep track of two things: the total fuel calculated and then _next_ amount of fuel to add. Once said amount is negative or zero, we have finished:

```python
def fuel_for_module(mass):
	def calc_fuel(mass):
		return math.floor(mass / 3) - 2

	# Get initial amount of fuel for mass
	total_fuel = 0
	next_fuel = calc_fuel(mass)

	# While we still have fuel to add
	while next_fuel > 0:
		total_fuel = total_fuel + next_fuel

		# Update next fuel with the needed for the last added
		next_fuel = calc_fuel(next_fuel)
```

<details>
	<summary>Solution</summary>

	Total sum of fuel is 5058559
</details>