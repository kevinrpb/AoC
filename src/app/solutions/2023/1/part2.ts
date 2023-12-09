import { readLines } from '@/lib/input'
import run from '@/lib/run'

const digits = [
  { digit: '1', regex: /one|1/g },
  { digit: '2', regex: /two|2/g },
  { digit: '3', regex: /three|3/g },
  { digit: '4', regex: /four|4/g },
  { digit: '5', regex: /five|5/g },
  { digit: '6', regex: /six|6/g },
  { digit: '7', regex: /seven|7/g },
  { digit: '8', regex: /eight|8/g },
  { digit: '9', regex: /nine|9/g },
]

const solve = async () => {
  // Our sum starts at zero.
  let sum = 0

  // Iterate over the lines.
  for (const line of readLines('2023/1')) {
    const lineNumbers = digits
      // For each digit, search it in the string and save the indices
      // where it appears.
      //
      // We use `flatMap` here to un-nest the array that we return.
      // That way, in the next operation we will have an 'array of items'
      // and not an 'array of array of items'.
      .flatMap(({ digit, regex }) =>
        // `matchAll` returns an iterable, we use the spread operator
        // to turn it into an array so we can `map` it.
        [...line.matchAll(regex)].map(({ index }) => ({ index: index ?? -1, digit }))
      )
      // Take out those that didn't match.
      .filter(({ index }) => index !== -1)
      // Sort remaining by index
      .sort((a, b) => a.index - b.index)
      // Get the digits, ordered
      .map(({ digit }) => digit)
      // concatenate them
      .join('')

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
