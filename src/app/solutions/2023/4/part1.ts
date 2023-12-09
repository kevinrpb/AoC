import { readLines } from '@/lib/input'
import run from '@/lib/run'
import { parseCardLine } from './common'

const solve = async () => {
  let sum = 0

  for (const line of readLines('2023/4')) {
    const card = parseCardLine(line)
    // console.log(JSON.stringify(card))

    const matchingNumbers = card.cardNumbers.filter((n) => card.winningNumbers.includes(n))
    const points = matchingNumbers.length < 1 ? 0 : Math.pow(2, matchingNumbers.length - 1)

    // console.log(`${card.id}: ${matchingNumbers} -> ${points}`)

    sum += points
  }

  console.log(`\nTotal sum is ${sum}!`)
}

run(solve)
