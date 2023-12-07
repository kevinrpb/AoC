import fs from 'node:fs/promises'

import { fromFile } from 'gen-readlines'

export const readFile = async (file: string): Promise<string> => {
  return (await fs.readFile(`inputs/${file}`)).toString()
}

export function* readLines(file: string): Generator<string> {
  for (const line of fromFile(`inputs/${file}`)) {
    yield line.toString()
  }
}
