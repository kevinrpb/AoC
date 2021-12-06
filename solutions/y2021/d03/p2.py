#! /usr/bin/env python3

from pathlib import Path

from statistics import mode, multimode
from typing import Callable

import numpy as np
from solutions.util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 3
AOC_PROBLEM = 2

# * UTIL

scriptpath = Path(__file__).parent.resolve()

SWAP = {
  '0': '1',
  '1': '0'
}

def parseLine(line: str):
  bits = list(line) # Get array of chars

  return bits

def getMostCommonBit(bits: list) -> str:
  # Multimode will account for when we have same ammount of 0s and 1s.
  # Then we can use this to select 1s in that case.
  most_common_bit = multimode(bits)

  if len(most_common_bit) > 1:
    most_common_bit = '1'
  else:
    most_common_bit = most_common_bit[0]

  return most_common_bit

def filterMatrix(matrix: np.matrix, most_common: bool = True) -> np.matrix:
  _matrix = matrix
  _transposed = _matrix.getT()

  for index in range(_transposed.shape[0]):
    if _matrix.shape[0] < 2:
      break

    # Get most common bit
    bits = _transposed.getA()[index]
    most_common_bit = getMostCommonBit(bits)

    if most_common:
      check_bit = most_common_bit
    else:
      check_bit = SWAP[most_common_bit]

    # Filter matrix
    _matrix = np.matrix(
      [row for row in _matrix.getA() if row[index] == check_bit])
    _transposed = _matrix.getT()

  return _matrix

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines

inputpath = scriptpath / Path('./input.txt')
inputLines = readFileLines(inputpath, parseLine)

print(f'There are {len(inputLines)} inputs\n')

# Get as matrix and transpose
matrix = np.matrix(inputLines)
transposed = matrix.getT()

#
o2_bits = filterMatrix(matrix, most_common=True).getA1()
co2_bits = filterMatrix(matrix, most_common=False).getA1()

# Get into a string
o2_str = ''.join(o2_bits)
co2_str = ''.join(co2_bits)

# Get integers
o2_int = int(o2_str, 2)
co2_int = int(co2_str, 2)
result = o2_int * co2_int

# Print
print(f'o2   = {o2_str} = {o2_int:8d}')
print(f'co2  = {co2_str} = {co2_int:8d}')
print(f'{"-"*32}')
print(f'{" "*18}* = {result:8d}')
