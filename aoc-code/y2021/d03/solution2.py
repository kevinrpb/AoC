#! /usr/bin/env python3

from pathlib import Path

from ...util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 3
AOC_PROBLEM = 2

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
horizontal = depth = aim = 0

for command, number in input_lines:
  if command == 'forward':
    horizontal += number
    depth += aim * number
  elif command == 'down':
    aim += number
  elif command == 'up':
    aim -= number

result = horizontal * depth

print(f'horizontal = {horizontal:10d}')
print(f'     depth = {depth:10d}')
print(f'{"-"*25}')
print(f'         * = {result:10d}')
