<!--
name: 'Tool result: REPL backtick template literal hint'
description: >-
  Hint appended to a REPL script error when two backticks made a string get
  called
ccVersion: 2.1.318
-->
Hint: two backticks in a row end one template literal and tag the next, so a string gets called. Text that contains backticks or `${` is safer in a '…' or "…" string, or read from a file.
