export interface Card {
  id: number
  winningNumbers: number[]
  cardNumbers: number[]
}

export const parseCardLine = (line: string): Card => {
  const id = parseInt((line.match(/^Card\s+([0-9]+):/) ?? [])[1])

  const numbers = line.split(':')[1]
  const [winningNumbers, cardNumbers] = numbers.split('|').map((numbersString) =>
    numbersString
      .trim()
      .split(/\s+/)
      .map((s) => parseInt(s))
  )

  return { id, winningNumbers, cardNumbers }
}
