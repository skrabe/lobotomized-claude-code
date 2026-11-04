<!--
name: 'Tool Result: REPL async dispatch cap rejected'
description: >-
  Rejects an async REPL dispatch when too many evals are already waiting or
  running and asks to wait for settles
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_ASYNC_DISPATCH_CAP_REJECTED_VAR_0
-->
async REPL dispatch rejected: ${TOOL_RESULT_REPL_ASYNC_DISPATCH_CAP_REJECTED_VAR_0.depth} evals already waiting or running on this context — wait for their settles (Poll) before dispatching more
