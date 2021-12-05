#! /usr/bin/env python3

from pathlib import Path

from solutions.util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 1
AOC_PROBLEM = 1

# * UTIL

scriptpath = Path(__file__).parent.resolve()

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines
inputpath = scriptpath / Path('./input.txt')
input_lines = readFileLines(inputpath, f = int)

print(f'There are {len(input_lines)} measurements')

# Count how many are deeper than previous
count = 0

for i in range(1, len(input_lines)):
  if input_lines[i] > input_lines[i - 1]:
    count += 1

#
print(f'\t -> {count} are deeper than the previous one')
