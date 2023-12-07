import { readLines } from '@/lib/input'
import run from '@/lib/run'
import { parseLine } from './common';

const solve = async () => {
  // Our sum starts at zero.
  let sum = 0;

  // Iterate over the lines.
  for (const line of readLines('2023/2')) {
    const { id, sets } = parseLine(line)

    console.log(line)
    console.log(`  id: ${id}`)
    console.log(`  sets (${sets.length}):`)
    for (const set of sets) {
      const { red, green, blue } = set
      console.log(`    r:${red} g:${green} b:${blue}`)
    }

    const { red, green, blue } = sets.reduce((currentMin, nextSet) => {
      return {
        red: Math.max(currentMin.red, nextSet.red),
        green: Math.max(currentMin.green, nextSet.green),
        blue: Math.max(currentMin.blue, nextSet.blue),
      }
    }, { red: 0, green: 0, blue: 0})
    const power = red * green * blue

    console.log(`  min: r:${red} g:${green} b:${blue}`)
    console.log(`  power: ${power}`)

    sum += power
  }

  // Print our total sum!
  console.log(`\nTotal sum is ${sum}`)
}

run(solve)
