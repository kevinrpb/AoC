#! /usr/bin/env python3

from pathlib import Path
from statistics import mode

import numpy as np
from solutions.util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 3
AOC_PROBLEM = 1

# * UTIL

scriptpath = Path(__file__).parent.resolve()

SWAP = {
  '0': '1',
  '1': '0'
}

def parseLine(line: str):
  bits = list(line) # Get array of chars

  return bits

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines

inputPath = scriptpath / Path('./input.txt')
inputLines = readFileLines(inputPath, parseLine)

print(f'There are {len(inputLines)} inputs\n')

# Get as matrix and transpose
matrix = np.matrix(inputLines)
transposed = matrix.getT()

# Get the most common bits using `mode`
gamma_bits = [mode(bits) for bits in transposed.getA()]
epsilon_bits = list(map(lambda bit: SWAP[bit], gamma_bits))

# Get into a string
gamma_str = ''.join(gamma_bits)
epsilon_str = ''.join(epsilon_bits)

# Get integers
gamma_int = int(gamma_str, 2)
epsilon_int = int(epsilon_str, 2)
result = gamma_int * epsilon_int

# Print
print(f'gamma   = {gamma_str} = {gamma_int:8d}')
print(f'epsilon = {epsilon_str} = {epsilon_int:8d}')
print(f'{"-"*40}')
print(f'{" "*21}* = {result:8d}')
