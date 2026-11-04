<!--
name: 'REPL: Call Arguments BigInt'
description: Refusal for a REPL inner tool call whose arguments contain a BigInt.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_0} ${TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_1} ${TOOL_RESULT_REPL_CALL_ARGS_BIGINT_VAR_2?"is or contains":"contain"} a BigInt, which can't be written as JSON. Pass a number or a string instead, such as Number(n) or String(n).
