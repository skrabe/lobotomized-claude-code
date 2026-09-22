<!--
name: Bash tool Git Bash note (Windows)
description: >-
  Windows-only note appended to the Bash tool description about Git Bash/POSIX
  syntax.
ccVersion: 2.1.206
-->
This tool runs Git Bash (POSIX sh), not cmd.exe or PowerShell. Use Unix shell syntax: `/dev/null` not `NUL`, forward slashes, `$VAR` not `%VAR%` or `$env:VAR`.
