import createMDX from '@next/mdx'
import rehypeHighlight from 'rehype-highlight'

import typescript from 'highlight.js/lib/languages/typescript'

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

const withMDX = createMDX({
  extension: /\.mdx?$/,
  options: {
    remarkPlugins: [],
    rehypePlugins: [[rehypeHighlight, { languages: { typescript }}]],
  },
})

export default withMDX(nextConfig)
