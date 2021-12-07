#! /usr/bin/env python3

from pathlib import Path
from statistics import mode

import numpy as np
from solutions.util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 4
AOC_PROBLEM = 1

# * UTIL

scriptpath = Path(__file__).parent.resolve()

def parseLine(line: str):
  line = line.replace('  ', ' ') # Change double spaces to 1 space
  line = line.lstrip()           # Remove leading space
  line = line.replace(' ', ',')  # Change spaces to commas

  if line == '\n' or line == '':
    return None

  return [int(n) for n in line.split(',')] # Parse integers and return as list

def parseGame(lines: list) -> tuple:
  draws = lines[0]
  boards = []

  current_board = -1 if lines[1] is None else 0
  for line in lines[1:]:
    # Go to next board
    if line is None:
      current_board += 1
      continue

    # Init board if needed
    if current_board >= len(boards):
      boards.append([])

    # Add line to board
    boards[current_board].append([(n, False) for n in line])

  draws = np.array(draws)
  boards = np.rec.array(boards, dtype=[('number', 'i'), ('marked', 'bool')])

  return draws, boards


# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines

inputPath = scriptpath / Path('./input.txt')
inputLines = readFileLines(inputPath, parseLine)

print(f'There are {len(inputLines)} inputs\n')

# Parse into drawn numbers and boards

draws, boards = parseGame(inputLines)

print(f'  -> We drew {draws.shape[0]} numbers')
print(f'  -> We have {boards.shape[0]} boards')

print(boards[0])

lastNumber = None
for i, number in enumerate(draws):
  lastNumber = number
