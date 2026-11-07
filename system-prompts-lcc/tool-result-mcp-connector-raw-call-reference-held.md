<!--
name: 'Tool Result: MCP connector raw call refused (sha256 reference)'
description: >-
  Refuses a raw connector call whose argument begins sha256: like a local file
  reference that would reach the connector as is
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_0} was not called: its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_REFERENCE_HELD_VAR_2)} begins sha256: (in either case), as a reference to a file on this machine does, and this call skips the tool's file handling, so what is written there would have gone to the connector as it is, a file's path and hash included where it holds them. Write there what the tool itself takes in that argument, or leave it out.
