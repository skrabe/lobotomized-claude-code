<!--
name: 'Bash tool result: Windows sandbox start path missing'
description: >-
  Explains Windows could not start the sandbox because a protected path cannot
  be reached (broken link, missing drive, removed folder), to fix it and
  restart, and how the backend setting can be changed.
ccVersion: 2.1.330
-->
Windows could not start the sandbox because a path it protects cannot be reached, for example behind a broken link, on a missing drive or in a folder that was removed. Fix that path and restart Claude Code. Whoever manages the sandbox settings can set sandbox.windows.backend to "sandboxuser" and run claude sandbox install to use the sandbox account backend at the next start of Claude Code
