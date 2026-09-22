<!--
name: 'Plugin validate: agent name falls back to the filename'
description: >-
  Consequence clause for a non-project agent whose frontmatter failed to parse:
  the name comes from the filename and every other field is dropped.
ccVersion: 2.1.233
-->
At runtime this agent loads with its name taken from the filename and every other frontmatter field silently dropped.
