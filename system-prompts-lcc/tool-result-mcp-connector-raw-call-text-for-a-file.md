<!--
name: 'Tool Result: MCP connector raw call refused (text for a file)'
description: >-
  Refuses a raw connector call whose file argument holds text that would reach
  the connector as plain text
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_0} was not called: its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_TEXT_FOR_A_FILE_VAR_2)} takes a file, and this call would have gone straight to the connector, which would have received what is written there as plain text and not a file. Leave that argument out: a call made this way cannot have a file uploaded for it.
