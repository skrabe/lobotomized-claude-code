<!--
name: shQuote PowerShell guidance
description: >-
  Fragment of the Execute-JavaScript tool description teaching the model how to
  quote shell args on PowerShell.
ccVersion: 2.1.206
-->
`shQuote(s)` is POSIX-only — for PowerShell, double the single quotes: `"'"+s.replaceAll("'", "''")+"'"`. For multi-line input use a here-string `@'\n...\n'@` (closing `'@` at column 0).
