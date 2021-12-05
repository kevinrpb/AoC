from pathlib import Path
from typing import Any, Callable

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
