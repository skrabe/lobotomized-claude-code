<!--
name: 'Tool Result: Bash sandbox MXC deny path has profile variable'
description: >-
  Bash refusal when a protected path contains
  %USERPROFILE%/%HOMEDRIVE%/%HOMEPATH% so it cannot be protected
ccVersion: 2.1.328
-->
The command did not run: a path the sandbox protects has %USERPROFILE%, %HOMEDRIVE% or %HOMEPATH% inside it, usually in the name of the working folder or an added folder, so it cannot be protected. Rename that folder, or fix the path in your settings, and restart Claude Code. The debug log names the path.
