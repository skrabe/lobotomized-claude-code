<!--
name: 'Tool result: Bash Windows set-up too long'
description: >-
  Tells the model a command was not run because the per-command set-up (e.g.
  CLAUDE_ENV_FILE hook text) fills the Windows shell limit.
ccVersion: 2.1.332
-->
Claude Code did not run this command: the set-up that it runs before each command takes up nearly all that the shell on Windows accepts. A shorter command will not help. The user needs to shorten that set-up, such as the text that hooks write to CLAUDE_ENV_FILE.
