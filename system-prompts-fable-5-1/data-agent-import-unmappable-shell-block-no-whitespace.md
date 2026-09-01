<!--
name: 'Data: Agent Import — Shell Block Missing Leading Whitespace'
description: >-
  `untranslatable` reason from the Gemini command translator; becomes a
  user-scope unmappable reason injected into the `/import` prompt and the
  import-to-claude-code SKILL.md.
ccVersion: 2.1.214
-->
Its `!{…}` block isn't preceded by whitespace — Claude Code's `` !`cmd` `` marker requires it, so the shell exec would be silently lost.
