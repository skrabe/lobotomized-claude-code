<!--
name: 'Tool Result: MCP connector raw call refused (sha256 reference in attachment)'
description: >-
  Refuses a raw connector call whose nth attachment field begins sha256: like a
  local file reference
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_4
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_0} was not called: the ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_1} of the ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_2} attachment in its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_3(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_4)} begins sha256: (in either case, after any white space), as a reference to a file on this machine does, and this call skips the tool's file handling, so what is written there would have gone to the connector as it is, a file's path and hash included where it holds them. Write there what the tool itself takes in an attachment's ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_IN_ENTRY_VAR_1}, or leave that attachment out.
