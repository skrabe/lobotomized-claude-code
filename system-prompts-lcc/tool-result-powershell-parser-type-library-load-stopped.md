<!--
name: 'Tool result: PowerShell parser stopped before type library load'
description: >-
  Parse error explaining a command names a type and library file PowerShell
  would load, so permission rules could not be fully checked.
ccVersion: 2.1.332
-->
This command has text like [name, path]. PowerShell reads that as a type and the library file that holds it, and loads the file while it reads the command. Claude Code stopped before that, so it could not fully check your permission rules.
