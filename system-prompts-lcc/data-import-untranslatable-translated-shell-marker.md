<!--
name: 'Data: Import untranslatable translated shell marker'
description: >-
  Unmappable-item reason for a translated body that gained a !`cmd` marker
  absent from the Gemini prompt, interpolated into the /import query prompt and
  the import-to-claude-code SKILL.md
ccVersion: 2.1.214
-->
Its translated body contains a `` !`cmd` `` shell-exec marker that wasn't a `!{…}` block in the Gemini prompt (inert there, live in Claude Code).
