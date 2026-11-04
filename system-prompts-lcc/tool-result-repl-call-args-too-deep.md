<!--
name: 'REPL: Call Arguments Too Deep'
description: >-
  Refusal for a REPL inner tool call whose arguments are nested too deep for
  JSON.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_0} ${TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_1} ${TOOL_RESULT_REPL_CALL_ARGS_TOO_DEEP_VAR_2?"is":"are"} nested too deep to be written as JSON. Pass a flatter value.
