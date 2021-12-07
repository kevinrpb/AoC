#! /usr/bin/env python3

from pathlib import Path

from statistics import mode, multimode
from typing import Callable

import numpy as np
from solutions.util.parse import readFileLines

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 4
AOC_PROBLEM = 2

# * UTIL

scriptpath = Path(__file__).parent.resolve()

def parseLine(line: str):
  bits = list(line) # Get array of chars

  return bits

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')
print(f'{"="*50}\n')

# Get the lines

inputpath = scriptpath / Path('./input.txt')
inputLines = readFileLines(inputpath, parseLine)

print(f'There are {len(inputLines)} inputs\n')
