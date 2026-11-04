<!--
name: 'Tool result: REPL pending calls discarded'
description: >-
  Warning in the REPL result that tool calls were still pending at script end
  and their results were discarded; add await.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALLS_PENDING_RESULTS_DISCARDED_VAR_0
  - TOOL_RESULT_REPL_CALLS_PENDING_RESULTS_DISCARDED_VAR_1
-->
⚠ ${TOOL_RESULT_REPL_CALLS_PENDING_RESULTS_DISCARDED_VAR_0.length} tool call(s) still pending at script end — results discarded: ${TOOL_RESULT_REPL_CALLS_PENDING_RESULTS_DISCARDED_VAR_1}. Add 'await'.
