<!--
name: 'Tool Result: MCP connector raw call refused (timeout used up)'
description: >-
  Refuses a raw connector call because waiting for the tool list used up the
  call's timeout
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NO_TIME_LEFT_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NO_TIME_LEFT_VAR_0} was not called: Claude Code waited for this connector's list of tools so that it could check this call, and that wait used up the call's timeout. Calling again in a moment may work.
