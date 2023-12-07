import { readLines } from '@/lib/input'
import run from '@/lib/run'

const solve = async () => {
  // Our sum starts at zero.
  let sum = 0

  // Iterate over the lines.
  for (const line of readLines('2023/1')) {
    // 'Erase' all non-number characters from the line
    const lineNumbers = line.replace(/[^0-9]/g, '')
    // Pick the first and last characters from the resulting string.
    // If there is only one character, it will be taken in both places.
    const firstNumber = lineNumbers.slice(0, 1)
    const lastNumber = lineNumbers.slice(-1)
    // Parse the resulting two-digits character into an integer. This
    // will allow us to add it to the sum.
    const number = parseInt(`${firstNumber}${lastNumber}`)

    console.log(`${line} | ${lineNumbers} | ${number}`)

    sum += number
  }

  // Print our total sum!
  console.log(`\nTotal sum is ${sum}`)
}

run(solve)
