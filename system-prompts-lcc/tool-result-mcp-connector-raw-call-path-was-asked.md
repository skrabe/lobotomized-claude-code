<!--
name: 'Tool Result: MCP connector raw call refused (path asked)'
description: >-
  Refuses a connector call that skips the tool's file handling for an argument
  Claude Code asked a file path for
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_0} was not called: Claude Code asked the model for a file's path in ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_WAS_ASKED_VAR_2)}, but this call skips the tool's file handling and would have passed that argument straight to the connector.
