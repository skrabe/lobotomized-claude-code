<!--
name: 'REPL: Dangerous Removal Check Failed'
description: >-
  Deny message when the REPL dangerous-removal check itself faulted; asks to
  resend the command alone with full paths.
ccVersion: 2.1.318
-->
This command was not run. The check for a dangerous removal failed because of a fault in Claude Code.
To run it, send it in a new call, as the only command, with full paths and with no change of folder or environment. It then gets the normal permission check.
