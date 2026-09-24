<!--
name: 'Tool Result: Tool Call Cancelled — Turn Ended On Error'
description: >-
  Error tool_result inserted for each open tool call when the turn ends on a
  model or API error, and carries the error text.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_TOOL_CALL_CANCELLED_TURN_ERROR_VAR_0
-->
The turn ended on an error, so this tool call was cancelled. If it had already started, some of its effects may have happened. Error: ${TOOL_RESULT_TOOL_CALL_CANCELLED_TURN_ERROR_VAR_0}
