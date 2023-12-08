import { readFile } from '@/lib/input'
import run from '@/lib/run'
import { getPartNumbers } from './common'

const solve = async () => {
  let input = await readFile('2023/3')
  let inputGrid = input.split('\n').map((line): string[] => Array.from(line))

  console.log(`nrows: ${inputGrid.length}`)
  console.log(`ncols: ${inputGrid[0].length}`)

  const partNumbers = getPartNumbers(inputGrid)

  console.log(`nparts: ${partNumbers.length}`)

  // for (const partNumber of partNumbers) {
  //   console.log(JSON.stringify(partNumber))
  // }

  // Sum the parts
  const partSum = partNumbers.reduce((sum, { value }) => sum + value, 0)

  console.log(`\nTotal sum is ${partSum}!`)
}

run(solve)
