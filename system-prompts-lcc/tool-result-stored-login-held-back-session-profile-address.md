<!--
name: 'Stored login held back: base URL changed'
description: >-
  Error that nothing was sent because ANTHROPIC_BASE_URL changed since the
  session started.
ccVersion: 2.1.332
-->
Nothing was sent: ANTHROPIC_BASE_URL was changed from what Claude Code was started with, so this session and its sign-in would go to another address. It usually comes from the "env" block of a settings file (/status shows the address in use). Remove it there, then exit and run claude --resume. If you reopen this session before removing it, the session may go to that address.
