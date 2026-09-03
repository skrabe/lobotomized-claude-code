<!--
name: Async REPL dispatch rejected — queue depth cap
description: >-
  REPL tool result returned when too many async evals are already queued or
  running, telling Claude to wait for their settles before dispatching more.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_REPL_ASYNC_DISPATCH_QUEUE_DEPTH_CAP_VAR_0
-->
async REPL dispatch rejected: ${TOOL_RESULT_REPL_ASYNC_DISPATCH_QUEUE_DEPTH_CAP_VAR_0} evals already queued or running — wait for their settles (Poll) before dispatching more
