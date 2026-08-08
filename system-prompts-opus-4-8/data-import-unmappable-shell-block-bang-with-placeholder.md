<!--
name: 'Data: Import Unmappable — Shell Block ''!'' With Placeholders'
description: >-
  Portability-blocker reason returned by the import shell-safety check; lands in
  unmappable[].reason and is interpolated into the generated
  import-to-claude-code SKILL.md and the /import preview prompt.
ccVersion: 2.1.214
-->
One of its shell blocks contains '!' while the command also has argument placeholders — a backtick in the typed arguments could re-pair the marker into executing text the block never consented to.
