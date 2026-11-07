<!--
name: 'Tool Result: MCP connector raw call refused (record unreachable)'
description: >-
  Refuses a raw connector call that could not be checked against the record of
  tools asked for file paths
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_CANNOT_TELL_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_CANNOT_TELL_VAR_0} was not called: Claude Code could not check this call against its record of which connector tools it asked file paths for, so it could not tell whether this call would send a path as plain text. Calling again may or may not work.
