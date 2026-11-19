<!--
name: 'Tool Result: Bash sandbox rules stale for folder'
description: >-
  Refusal when sandbox rules could not be rebuilt for the current folder after a
  move, so sandboxed commands are refused
ccVersion: 2.1.328
-->
Sandboxed commands are refused: the sandbox rules could not be rebuilt for this folder, and the rules in force were made for another one. Running outside the sandbox (dangerouslyDisableSandbox) is refused too, so retrying will not help. A settings change that lets the rules rebuild lifts this, and so does moving the session back or restarting. `!` commands and commands excluded from the sandbox in settings still run.
