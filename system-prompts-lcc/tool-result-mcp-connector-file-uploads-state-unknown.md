<!--
name: 'Tool Result: MCP connector file upload state unknown'
description: >-
  Refuses a file call because Claude Code cannot tell whether connector file
  sending is on, allowing a later retry
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_STATE_UNKNOWN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_STATE_UNKNOWN_VAR_1
-->
No file was sent: Claude Code cannot tell just now whether sending files to connectors is on. ${TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_STATE_UNKNOWN_VAR_0(TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_STATE_UNKNOWN_VAR_1)} Tell the user; a call that names a file can be tried again later. Calls that name no file still work.
