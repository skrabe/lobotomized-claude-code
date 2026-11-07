<!--
name: Connector upload state unknown
description: >-
  Says no file was sent because Claude Code can no longer tell whether connector
  file sending is on.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_PROMPT_STATE_UNKNOWN_VAR_0
-->
No file was sent: since the approval prompt was shown, Claude Code can no longer tell whether sending files to connectors is on. Tell the user; the call can be tried again later. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_PROMPT_STATE_UNKNOWN_VAR_0}
