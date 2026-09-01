<!--
name: 'Data: Import untranslatable backtick in shell block'
description: >-
  Unmappable-item reason for a !{…} block containing a backtick, interpolated
  into the /import query prompt and the import-to-claude-code SKILL.md
ccVersion: 2.1.214
-->
Its `!{…}` shell block contains a backtick, which Claude Code's `` !`cmd` `` syntax can't represent.
