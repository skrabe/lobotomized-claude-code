<!--
name: 'Tool result: REPL call args too large for long list'
description: >-
  Error when REPL call arguments exceed the JSON character limit for argument
  sets with long lists.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_0} its arguments are longer than ${TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_1.textChars.toLocaleString("en-US")} characters as JSON, the limit when they have a list of over ${TOOL_RESULT_REPL_CALL_ARGS_TOO_LARGE_LONG_LIST_VAR_2.toLocaleString("en-US")} items. Send the items in several calls.
