import React from 'react'

import Link from 'next/link'

import './styles.scss'

const Header: React.FC = () => (
  <header>
    <h1 id='home-link'>
      <Link href='/'>Advent of Solutions</Link>
    </h1>

    <h1 id='year-link'>
      <span>sol y&#123;</span>
      <Link href='/solutions/2023'>2023</Link>
      <span>&#125;</span>
    </h1>

    <nav>
      <Link href='/solutions'>[All Solutions]</Link>
      <Link href='https://adventofcode.com'>[adventofcode.com]</Link>
      <Link href='https://kevinrpb.me'>[kevinrpb.me]</Link>
    </nav>
  </header>
)

export default Header
