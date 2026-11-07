<!--
name: 'Tool Result: MCP connector raw call refused (argument list unavailable)'
description: >-
  Refuses a raw connector call when the connector's current argument list is
  unavailable and suggests reconnecting via /mcp
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NAMES_NOT_AT_HAND_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NAMES_NOT_AT_HAND_VAR_0} was not called: Claude Code asked the model for a file's path for ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NAMES_NOT_AT_HAND_VAR_0} but does not have ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NAMES_NOT_AT_HAND_VAR_0}'s current list of arguments, so it could not check that no path is written as an argument's name. Calling again may or may not work: reconnecting the connector lists its tools again (in a terminal: /mcp), and the call then passes only if ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NAMES_NOT_AT_HAND_VAR_0} lists every argument the call sets.
