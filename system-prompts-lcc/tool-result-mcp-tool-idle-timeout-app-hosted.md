<!--
name: 'Tool result: MCP tool idle timeout (app-hosted server)'
description: >-
  Error returned when an SDK/app-hosted MCP server's tool sent no response or
  progress for the idle window and Claude Code stopped waiting
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_0
  - TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_1
  - TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_2
  - TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_3
-->
MCP server "${TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_0}" tool "${TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_1}" sent no response or progress for ${TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_2}s, so Claude Code stopped waiting for it. This server runs in the app that hosts this session. ${TOOL_RESULT_MCP_TOOL_IDLE_TIMEOUT_APP_HOSTED_VAR_3}
