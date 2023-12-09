export interface PartNumber {
  row: number
  columns: [number, number]
  size: number
  value: number
}

const NUMBERS = '0123456789'
const SYMBOLS = '!@#$%&=?+-*/'

const processPartNumber = (
  grid: string[][],
  row: number,
  startColumn: number,
  endColumn: number,
  validSymbols: string
): PartNumber | undefined => {
  // Check around the number. If at any point we find a symbol, return
  // the part.
  for (let rowIndex = row - 1; rowIndex <= row + 1; rowIndex++) {
    // If we are out of bounds, skip.
    if (rowIndex < 0 || rowIndex >= grid.length) {
      continue
    }

    for (let columnIndex = startColumn - 1; columnIndex <= endColumn + 1; columnIndex++) {
      // If we are out of bounds, skip.
      if (columnIndex < 0 || columnIndex >= grid[rowIndex].length) {
        continue
      }

      const character = grid[rowIndex][columnIndex]

      // If the character is not a number or a period, then it's a symbol.
      if (validSymbols.includes(character)) {
        const numberLine = grid[row]
        const numberString = numberLine.slice(startColumn, endColumn + 1).join('')

        return {
          row,
          columns: [startColumn, endColumn],
          size: numberString.length,
          value: parseInt(numberString),
        }
      }
    }
  }

  // If we get to here, we did not find a symbol.
  return undefined
}

export const getPartNumbers = (grid: string[][], validSymbols: string = SYMBOLS): PartNumber[] => {
  let partNumbers: PartNumber[] = []

  for (const [row, line] of grid.entries()) {
    let numberStartColumn: number | undefined = undefined

    for (const [column, character] of line.entries()) {
      // console.log(`[${row},${column}]: ${character}`)

      // Check whether it's a number
      if (NUMBERS.includes(character)) {
        // If we were not tracking another number, then this one starts one
        if (numberStartColumn === undefined) {
          numberStartColumn = column
        }
        // If we were already tracking a number, then we don't do anything
        // until we find something that is not a number
      } else {
        // If we reach something that is not a number but we were tracking
        // one, then we process it.
        if (numberStartColumn !== undefined) {
          const newNumber = processPartNumber(
            grid,
            row,
            numberStartColumn,
            column - 1,
            validSymbols
          )

          // If the number is actually a part, save it.
          if (newNumber !== undefined) {
            partNumbers.push(newNumber)
          }

          // Reset to look for more parts.
          numberStartColumn = undefined
        }
      }
    }

    // When we are done with a line, if we were tracking a number then we
    // process it.
    if (numberStartColumn !== undefined) {
      const newNumber = processPartNumber(
        grid,
        row,
        numberStartColumn,
        line.length - 1,
        validSymbols
      )

      // If the number is actually a part, save it.
      if (newNumber !== undefined) {
        partNumbers.push(newNumber)
      }
    }
  }

  return partNumbers
}
