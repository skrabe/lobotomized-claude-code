<!--
name: 'Data: Import Warning — Gemini Shell-Exec Command'
description: >-
  Warning attached to an importable Gemini command that uses !{cmd}; BA_()
  appends it to the item line in the {type:'query'} prompt /import sends to the
  model.
ccVersion: 2.1.214
-->
Uses `!{cmd}` shell exec — import grants the command `allowed-tools: [Bash, PowerShell]` (any shell command, not just the named ones) and marks it `disable-model-invocation` so, like the Gemini original, only you can run it via `/name`. Unchecked by default; review before importing.
