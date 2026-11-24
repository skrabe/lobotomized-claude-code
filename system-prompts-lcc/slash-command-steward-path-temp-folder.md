<!--
name: 'Slash Command: Steward - PATH in session temp folder'
description: >-
  /steward reason that PATH holds a folder inside Claude Code's temporary
  folder, so it cannot tell which gh and git would run, with advice to start
  claude without it.
ccVersion: 2.1.331
-->
your PATH includes a folder inside Claude Code's temporary folder, where this session can write, so it isn't clear which gh and git would run. Start claude from a shell without that folder, which echo $PATH shows
