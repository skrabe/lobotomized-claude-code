<!--
name: 'Tool result: MCP connector upload asked twice'
description: >-
  Connector upload error: the connector asked for files again, which Claude Code
  does not answer.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ASKED_TWICE_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ASKED_TWICE_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ASKED_TWICE_VAR_0.length===0?"The connector asked for files again when the call was repeated":"The connector asked for this call's files a second time"}, which Claude Code does not answer. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ASKED_TWICE_VAR_1}
