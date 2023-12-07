import type { Metadata } from 'next'

import '@/styles/global.scss'
import Header from '@/components/header'

export const metadata: Metadata = {
  title: 'Advent of Code Solutions',
  description: '',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='en'>
      <body>
        <Header />
        {children}
      </body>
    </html>
  )
}
