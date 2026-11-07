<!--
name: Connector upload stopped after prompt
description: >-
  Says no file was sent because Claude Code stopped connector file sending this
  session after the approval prompt.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STOPPED_AFTER_PROMPT_VAR_0
-->
No file was sent: Claude Code stopped sending files to connectors in this session after the approval prompt was shown. Tell the user; do not retry. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STOPPED_AFTER_PROMPT_VAR_0}
