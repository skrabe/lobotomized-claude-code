<!--
name: 'Data: Agent Import — Translation Would Introduce Shell Exec'
description: >-
  `untranslatable` reason when translation would make an inert Gemini string
  execute a shell command; surfaced as a user-scope unmappable in the `/import`
  prompt and SKILL.md.
ccVersion: 2.1.214
-->
Its translated body would execute a shell command that wasn't a `!{…}` block in the Gemini prompt (inert there, live in Claude Code).
