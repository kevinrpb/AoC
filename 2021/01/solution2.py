#! /usr/bin/env python3

from pathlib import Path
from typing import Any, Callable

# * INFO

AOC_YEAR    = 2021
AOC_DAY     = 1
AOC_PROBLEM = 1

# * UTIL

scriptpath = Path(__file__).parent.resolve()

def readFileLines(filepath: Path, f: Callable[[str], Any] = str) -> list:
  """Reads the lines in a file

  Args:
      filepath (Path): The path of the file to be read.
      f (Callable[[str], Any], optional): Transformation for the lines. Defaults to `str`.

  Returns:
      list: list with the lines, with the defined transformation applied.
  """
  lines = None

  with open(filepath, 'r') as file:
    lines = []

    # `readline` reads one line (better do it like this for large files)
    # `strip` removes leading/trailing whitespace
    while (line := file.readline().strip()):
      lines.append(f(line)) # We want integer numbers

  return lines

def getWindows(array: list, size: int = 3) -> list:
  windows = []

  for i in range((size-1), len(array)):
    w = array[i]

    for j in range(1, size):
      w += array[i - j]

    windows.append(w)

  return windows

# * MAIN

print(f'Advent of Code - {AOC_YEAR} - Day {AOC_DAY:02d} - Problem {AOC_PROBLEM:02d}')

# Get the lines
inputpath = scriptpath / Path('./input.txt')
input_lines = readFileLines(inputpath, f = int)

print(f'There are {len(input_lines)} measurements')

# Calculate windows
windows = getWindows(input_lines, size=3)

print(f'There are {len(windows)} measurement windows')

# Count how many are deeper than previous
count = 0

for i in range(1, len(windows)):
  if windows[i] > windows[i - 1]:
    count += 1

#
print(f'\t -> {count} are deeper than the previous one')
