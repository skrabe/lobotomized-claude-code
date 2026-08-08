<!--
name: 'Data: Import untranslatable shell block dropped'
description: >-
  Unmappable-item reason from the foreign-agent importer, interpolated into the
  /import query prompt sent to the model and into the generated
  import-to-claude-code SKILL.md
ccVersion: 2.1.214
-->
A `!{…}` shell block would be silently dropped by Claude Code's `` !`cmd` `` parsing after translation (its marker re-pairs with nearby backticks).
