<!--
name: 'REPL Tool Parameter: timeout'
description: >-
  Describes the REPL tool's optional timeout input: the script's own running
  time limit in ms, excluding awaited tool calls, with default and max.
ccVersion: 2.1.318
-->
Optional limit on the script's own running time in milliseconds; time spent inside the tool calls it awaits is not counted (default 30000, max 600000)
