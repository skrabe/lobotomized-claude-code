<!--
name: 'Tool Result: MCP connector raw call refused (held for a file)'
description: >-
  Refuses a raw connector call that would pass a file argument straight to the
  connector
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_0} was not called: its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_HELD_FOR_A_FILE_VAR_2)} takes a file, but this call skips the tool's file handling and would have passed that argument straight to the connector.
