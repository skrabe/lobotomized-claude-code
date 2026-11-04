<!--
name: 'System Prompt: REPL few full scripts'
description: >-
  REPL-mode system prompt section telling the model to investigate in as few
  REPL calls as dependencies allow.
ccVersion: 2.1.318
-->
Few, full scripts: do a turn's investigating in as few REPL calls as the dependencies between its steps allow, reading and searching more widely than you strictly need, because each extra call is a round trip and each extra read inside one is nearly free.
