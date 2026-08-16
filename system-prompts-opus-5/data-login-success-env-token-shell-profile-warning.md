<!--
name: 'Data: Login success — a shell-profile token overrides the new one'
description: >-
  Warns that a token set in a shell profile or a Claude Code settings file keeps
  being used by new sessions until it is removed there.
ccVersion: 2.1.233
-->
but if that variable is set in your shell profile or a Claude Code settings file, new `claude` sessions will keep using the old token until you remove it there.
