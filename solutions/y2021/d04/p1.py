#! /usr/bin/env python3

from collections import Counter
from pathlib import Path

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

def checkBoards(boards):
  for index, board in enumerate(boards):
    # Check rows
    for rowIndex in range(board.shape[0]):
      markedCount = Counter(board.marked[rowIndex])[True]

      if markedCount == board.shape[1]:
        return index, board

    for columnIndex in range(board.shape[1]):
      markedCount = Counter(board.marked[:,columnIndex])[True]

      if markedCount == board.shape[0]:
        return index, board

  return None, None

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

lastDraw = None
winnerIndex = None
winnerBoard = None
for index, draw in enumerate(draws):
  # Save last draw
  lastDraw = draw

  # Mark numbers
  boards.marked[boards.number == draw] = True

  # We can start winning when we have at least 5 draws. This is a small
  # optimization that becomes important with many boards to check
  if index > 4:
    # Check for winner
    winnerIndex, winnerBoard = checkBoards(boards)

    if winnerBoard is not None:
      break

if winnerBoard is None:
  print('  -> None of the boards won')
  exit()

boardScore = sum(winnerBoard.number[winnerBoard.marked == False])
result = boardScore * lastDraw

print(f'  -> Board #{winnerIndex+1} (of {boards.shape[0]}) won\n')

print(f'score    = {boardScore:6d}')
print(f'lastDraw = {lastDraw:6d}')
print(f'{"-"*40}')
print(f'{" "*7}* = {result:6d}')
