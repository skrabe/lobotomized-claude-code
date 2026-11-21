<!--
name: 'Tool Result: Mod vcs.isolate bad arguments'
description: >-
  Argument check refusal for $.vcs.isolate describing the expected { name, from,
  for, base } shape.
ccVersion: 2.1.330
-->
takes { name, from, for, base } (from absolute, for "agent" or "session", base "fresh" or "head")
