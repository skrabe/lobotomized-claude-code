<!--
name: 'Tool Result: MCP tool may send files ask'
description: >-
  Permission ask message for an MCP tool marked as able to send the session's
  files elsewhere; becomes the tool_result the model reads if the ask is
  declined.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_MCP_TOOL_MAY_SEND_FILES_ASK_VAR_0
  - TOOL_RESULT_MCP_TOOL_MAY_SEND_FILES_ASK_VAR_1
-->
${TOOL_RESULT_MCP_TOOL_MAY_SEND_FILES_ASK_VAR_0.mcpInfo?.TOOL_RESULT_MCP_TOOL_MAY_SEND_FILES_ASK_VAR_1} can send this session's files elsewhere, so Claude asks before using it. Allow it if you expected this.
