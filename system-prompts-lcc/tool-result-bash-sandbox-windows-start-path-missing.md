<!--
name: 'Bash tool result: Windows sandbox start path missing'
description: >-
  Explains Windows could not start the sandbox because a requested path does not
  exist, and how the backend setting can be changed.
ccVersion: 2.1.326
-->
Windows could not start the sandbox because a path in the request does not exist, usually a deny entry under a missing folder such as .claude. Whoever manages the sandbox settings can set sandbox.windows.backend to "sandboxuser", or remove it, to use the sandbox account backend at the next start of Claude Code
