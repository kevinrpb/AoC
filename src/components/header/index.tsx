import React from 'react'

import Link from 'next/link'

import './styles.scss'

const Header: React.FC = () => (
  <header>
    <h1 id='home-link'>
      <Link href='/'>Advent of Code</Link>
    </h1>

    <h1 id='year-link'>
      <span>sol y&#123;</span>
      <Link href='/solutions/2023'>2023</Link>
      <span>&#125;</span>
    </h1>

    <nav>
      <Link href='/solutions'>[Solutions]</Link>
    </nav>
  </header>
)

export default Header
