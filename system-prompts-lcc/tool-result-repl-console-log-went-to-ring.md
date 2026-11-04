<!--
name: 'Tool result: REPL console.log went to ring'
description: >-
  Stdout note that console.log lines went to the console ring, not output; use
  self.log or console.tail().
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CONSOLE_LOG_WENT_TO_RING_VAR_0
  - TOOL_RESULT_REPL_CONSOLE_LOG_WENT_TO_RING_VAR_1
-->
[console.log wrote ${TOOL_RESULT_REPL_CONSOLE_LOG_WENT_TO_RING_VAR_0} ${TOOL_RESULT_REPL_CONSOLE_LOG_WENT_TO_RING_VAR_1(TOOL_RESULT_REPL_CONSOLE_LOG_WENT_TO_RING_VAR_0,"line")} to the console ring, not to this output — use self.log(...) for output you want to see, or read the ring with console.tail()]
