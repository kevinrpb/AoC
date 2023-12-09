import { readLines } from '@/lib/input'
import run from '@/lib/run'
import { parseCardLine } from './common'

const solve = async () => {
  let numberOfOriginals = 0
  let cardCopies: Record<number, number> = {}

  for (const line of readLines('2023/4')) {
    const card = parseCardLine(line)
    // Calculate the multiplier, which is the original card plus the number of copies.
    const multiplier = 1 + (cardCopies[card.id] ?? 0)

    const matchingNumbers = card.cardNumbers.filter((n) => card.winningNumbers.includes(n))
    const addedCopies = Array.from(
      { length: matchingNumbers.length },
      (_, number) => number + card.id + 1
    )

    console.log(`${card.id} -> + x${multiplier}[${addedCopies}]`)

    for (const id of addedCopies) {
      cardCopies[id] = (cardCopies[id] ?? 0) + multiplier
      console.log(`  ${id}: ${cardCopies[id]}`)
    }

    numberOfOriginals += 1
  }

  const numberOfCards =
    numberOfOriginals + Object.values(cardCopies).reduce((sum, copies) => sum + copies, 0)

  console.log(`\n There were a total of ${numberOfCards} cards!`)
}

run(solve)
