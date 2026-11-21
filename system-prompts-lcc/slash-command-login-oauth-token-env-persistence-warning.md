<!--
name: 'Slash command: /login OAuth token env persistence warning'
description: >-
  Warns that a CLAUDE_CODE_OAUTH_TOKEN set in a profile or settings file keeps
  new sessions on the old token
ccVersion: 2.1.330
-->
If CLAUDE_CODE_OAUTH_TOKEN is set in your shell profile or a Claude Code settings file, new `claude` sessions will keep using the old token until you remove it there.
