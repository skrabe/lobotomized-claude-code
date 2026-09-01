<!--
name: 'Agent Prompt: CLAUDE.md creation'
description: >-
  System prompt for analyzing codebases and creating CLAUDE.md documentation
  files
ccVersion: 2.1.214
-->
Analyze this codebase and create a CLAUDE.md file for future Claude Code instances working in this repo. If one already exists, suggest improvements to it.

Include:
1. Commonly used commands — build, lint, run tests (including how to run a single test).
2. Big-picture architecture: the structure that requires reading multiple files to understand.

If there are Cursor rules (.cursor/rules/ or .cursorrules), Copilot rules (.github/copilot-instructions.md), or a README.md, fold in the important parts.

Don't: repeat yourself; list components or file structure that's easily discovered; include generic dev practices or obvious instructions ("write unit tests", "don't commit secrets"); or invent sections like "Common Development Tasks" or "Tips for Development" that aren't grounded in files you actually read.

Prefix the file with:

\`\`\`
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
\`\`\`
