<!--
name: 'Data: Import Unmappable — Shell Block Argument Placeholder'
description: >-
  Portability-blocker reason for a Gemini shell block containing an argument
  placeholder; interpolated into the generated import-to-claude-code SKILL.md
  and the /import preview prompt.
ccVersion: 2.1.214
-->
One of its shell blocks contains an argument placeholder — Gemini shell-escapes `{{args}}` inside `!{…}`, Claude Code's `$ARGUMENTS` substitution doesn't, so importing would let typed arguments inject shell commands. Port it manually.
