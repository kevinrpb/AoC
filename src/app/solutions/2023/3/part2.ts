import { readFile } from '@/lib/input'
import run from '@/lib/run'
import { PartNumber, getPartNumbers } from './common'

interface Gear {
  row: number
  column: number
  numbers: [number, number]
  ratio: number
}

const GEAR = '*'

const getPartNumbersAroundGear = (
  partNumbers: PartNumber[],
  gearRow: number,
  gearColumn: number
): PartNumber[] => {
  return partNumbers.filter(({row, columns: [startColumn, endColumn]}) => {
    // If the number is not within one row of the gear then it cannot be adjacent.
    if (Math.abs(gearRow - row) > 1){
      return false
    }

    // For numbers in the same row
    if (gearRow === row) {
      // If the number ends before the gear or starts after the gear (with
      // one column in between), then it is not adjacent.
      if (gearColumn - endColumn > 1 || startColumn - gearColumn > 1) {
        return false
      }

      // Otherwise, the number must be adjacent!
      return true
    }

    // For numbers above or below, they must start or end within one column
    // to be adjacent.
    return Math.abs(gearColumn - startColumn) <= 1
        || Math.abs(gearColumn - endColumn) <= 1
  })
}

const getGears = (grid: string[][], partNumbers: PartNumber[]): Gear[] => {
  let gears: Gear[] = []

  for (const [row, line] of grid.entries()) {
    for (const [column, character] of line.entries()) {
      // If we find a gear, search around for part numbers.
      if (character === GEAR) {
        const partNumbersAround = getPartNumbersAroundGear(partNumbers, row, column)
        // console.log(`[${row}, ${column}] Around: ${JSON.stringify(partNumbersAround)}`)

        // We only take the gear if it has exactly two part numbers around.
        if (partNumbersAround.length === 2) {
          const [numberA, numberB] = partNumbersAround.map(({ value }) => value)

          gears.push({
            row,
            column,
            numbers: [numberA, numberB],
            ratio: numberA * numberB
          })
        }
      }
    }
  }

  return gears
}

const solve = async () => {
  let input = await readFile('2023/3')
  let inputGrid = input.split('\n').map((line): string[] => Array.from(line))

  // Get the part numbers, but only those adjacent to possible gears!
  const partNumbers = getPartNumbers(inputGrid, GEAR)
  const gears = getGears(inputGrid, partNumbers)

  console.log(`ngears: ${gears.length}`)

  // for (const gear of gears) {
  //   console.log(JSON.stringify(gear))
  // }

  // Sum the parts
  const gearSum = gears.reduce((sum, { ratio }) => sum + ratio, 0)

  console.log(`\nTotal sum is ${gearSum}!`)
}

run(solve)
