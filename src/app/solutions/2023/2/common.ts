export type CubeColor = 'red' | 'green' | 'blue'
export type CubeSet = Record<CubeColor, number>

export interface GameData {
  id: number
  sets: CubeSet[]
}

export const getGameId = (line: string): number => {
  const idMatch = line.match(/^Game ([0-9]+)\:/) ?? []

  return parseInt(idMatch[1])
}

export const parseSet = (setString: String): CubeSet => {
  const redMatch = setString.match(/([0-9]+) red/) ?? []
  const greenMatch = setString.match(/([0-9]+) green/) ?? []
  const blueMatch = setString.match(/([0-9]+) blue/) ?? []

  return {
    red: parseInt(redMatch[1] ?? '0'),
    green: parseInt(greenMatch[1] ?? '0'),
    blue: parseInt(blueMatch[1] ?? '0'),
  }
}

export const getGameSets = (line: string): CubeSet[] => {
  return line.split(':')[1]
    .split(';')
    .map(parseSet)
}

export const parseLine = (line: string): GameData => {
  const id = getGameId(line)
  const sets = getGameSets(line)

  return { id, sets }
}
