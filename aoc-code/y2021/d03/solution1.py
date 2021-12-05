#! /usr/bin/env python3

from pathlib import Path
from typing import Any, Callable

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 3
AOC_PROBLEM = 1

# * UTIL

scriptpath = Path(__file__).parent.resolve()



def parseLine(line: str) -> tuple:
  elements = line.split(' ')
  command = elements[0]
  number = int(elements[1])

  return (command, number)

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines

inputpath = scriptpath / Path('./input.txt')
input_lines = readFileLines(inputpath, parseLine)

print(f'There are {len(input_lines)} commands\n')

#
horizontal = depth = 0

for command, number in input_lines:
  if command == 'forward':
    horizontal += number
  elif command == 'down':
    depth += number
  elif command == 'up':
    depth -= number

result = horizontal * depth

print(f'horizontal = {horizontal:8d}')
print(f'     depth = {depth:8d}')
print(f'{"-"*20}')
print(f'         * = {result:8d}')
