<!--
name: 'REPL: Call Arguments Circular'
description: >-
  Refusal for a REPL inner tool call whose arguments contain a circular
  reference and cannot be written as JSON.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_0} ${TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_1} ${TOOL_RESULT_REPL_CALL_ARGS_CIRCULAR_VAR_2?"contains":"contain"} a circular reference, which can't be written as JSON. Copy the fields that the tool needs into a new object, and pass that.
