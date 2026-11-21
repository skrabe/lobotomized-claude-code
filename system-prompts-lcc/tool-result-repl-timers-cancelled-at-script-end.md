<!--
name: 'Tool result: REPL timers cancelled at script end'
description: >-
  Warning that sleep() calls or timers still waiting when the script ended were
  cancelled, with guidance for awaited loops.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_TIMERS_CANCELLED_AT_SCRIPT_END_VAR_0
-->
⚠ ${TOOL_RESULT_REPL_TIMERS_CANCELLED_AT_SCRIPT_END_VAR_0} sleep() or timer(s) were still waiting at script end and were cancelled. Ignore this if they were only timeouts. A loop that waited on one goes no further: to run it, await it inside one script (set the timeout parameter if it is long).
