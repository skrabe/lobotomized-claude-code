<!--
name: 'Tool Result: ListAgents next-page call arguments'
description: >-
  Fragment naming the arguments (cursor, plus channel and q when focused) for
  calling ListAgents again for the next page
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LISTAGENTS_NEXT_PAGE_CALL_ARGS_VAR_0
  - TOOL_RESULT_LISTAGENTS_NEXT_PAGE_CALL_ARGS_VAR_1
-->
with ${TOOL_RESULT_LISTAGENTS_NEXT_PAGE_CALL_ARGS_VAR_0.didFocused?"the same channel, the same q if any, and ":""}cursor="${TOOL_RESULT_LISTAGENTS_NEXT_PAGE_CALL_ARGS_VAR_1}"
