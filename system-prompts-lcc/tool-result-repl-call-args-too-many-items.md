<!--
name: 'Tool result: REPL call args too many items'
description: >-
  Error when typed arrays and long lists in REPL call arguments exceed the total
  item limit.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_0
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_1
  - TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_2
-->
${TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_0} the typed arrays and the lists of over ${TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_1.toLocaleString("en-US")} items in its arguments have more than ${TOOL_RESULT_REPL_CALL_ARGS_TOO_MANY_ITEMS_VAR_2.longItems.toLocaleString("en-US")} items together. Send the items in several calls, or pass bytes as base64 text.
