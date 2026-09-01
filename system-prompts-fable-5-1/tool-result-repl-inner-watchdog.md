<!--
name: REPL inner tool watchdog
description: >-
  Error surfaced to the model when a REPL inner tool call exceeds the watchdog
  timeout.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_REPL_INNER_WATCHDOG_VAR_0
  - TOOL_RESULT_REPL_INNER_WATCHDOG_VAR_1
-->
REPL inner tool call ${TOOL_RESULT_REPL_INNER_WATCHDOG_VAR_0.toolName} exceeded ${TOOL_RESULT_REPL_INNER_WATCHDOG_VAR_1}ms watchdog (native timeout ${TOOL_RESULT_REPL_INNER_WATCHDOG_VAR_0.nativeTimeoutMs??"unset"}). The call may be hung — try a shorter timeout on the tool itself.
