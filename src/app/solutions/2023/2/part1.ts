import { readLines } from '@/lib/input'
import run from '@/lib/run'
import { CubeSet, parseLine } from './common';

const maxCubes: CubeSet = {
  red: 12,
  green: 13,
  blue: 14
}

const solve = async () => {
  // Our sum starts at zero.
  let sum = 0;

  // Iterate over the lines.
  for (const line of readLines('2023/2')) {
    const { id, sets } = parseLine(line)

    const validSets = sets
      .filter(({ red, green, blue }) => red <= maxCubes.red && green <= maxCubes.green && blue <= maxCubes.blue)
    const gameIsValid = sets.length === validSets.length

    console.log(line)
    console.log(`  id: ${id}`)
    console.log(`  valid: ${gameIsValid}`)
    console.log(`  sets (${sets.length}):`)
    for (const set of sets) {
      const { red, green, blue } = set
      const setIsValid = red <= maxCubes.red && green <= maxCubes.green && blue <= maxCubes.blue
      console.log(`    r:${red} g:${green} b:${blue} ${setIsValid ? '' : 'X'}`)
    }

    if (gameIsValid) {
      sum += id
    }
  }

  // Print our total sum!
  console.log(`\nTotal sum is ${sum}`)
}

run(solve)
