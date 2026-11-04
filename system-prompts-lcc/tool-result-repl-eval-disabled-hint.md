<!--
name: 'Tool result: REPL eval disabled hint'
description: >-
  Hint appended to a REPL script error when eval/Function code generation is
  refused
ccVersion: 2.1.318
-->
Hint: `eval` and the `Function` constructors are off in this context by design, so a script cannot run a string as code here. To reload helpers saved in a file, read it, then send its text as the code of its own call: its top-level declarations stay defined for later calls.
