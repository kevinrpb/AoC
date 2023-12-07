const defaultError = (error: any) => {
  console.error(error)
}

const run = <T> (
  f: () => Promise<T>,
  thenCallback: ((t: T) => Promise<void>) | undefined = undefined,
  catchCallback: ((r: any) => Promise<void>) | undefined = undefined
) => {
  f().then(thenCallback).catch(catchCallback ?? defaultError)
}

export default run
