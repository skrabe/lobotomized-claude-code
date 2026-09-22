<!--
name: 'Data: Import untranslatable literal shell marker'
description: >-
  Unmappable-item reason for a Gemini prompt with a literal !` outside any shell
  block, interpolated into the /import query prompt and the
  import-to-claude-code SKILL.md
ccVersion: 2.1.214
-->
It has a literal `` !` `` outside any `!{…}` block (inert in Gemini, live in Claude Code — and it may pair with a translated block's backtick to run something other than the block).
