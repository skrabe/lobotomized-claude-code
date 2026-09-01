<!--
name: REPL wall-clock limit
description: >-
  Error surfaced to the model when REPL execution exceeds the hard wall-clock
  limit.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_REPL_WALLCLOCK_LIMIT_VAR_0
-->
REPL execution exceeded hard wall-clock limit of ${TOOL_RESULT_REPL_WALLCLOCK_LIMIT_VAR_0}ms. An inner tool call may be hung — try a shorter timeout on the tool itself, or split the work.
