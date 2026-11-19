<!--
name: 'Tool Result: MCP hook details left out'
description: >-
  Gives the MCP hook failure reason and says details are only in the debug log
  since the server may have written them
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MCP_HOOK_DETAILS_LEFT_OUT_VAR_0
  - TOOL_RESULT_MCP_HOOK_DETAILS_LEFT_OUT_VAR_1
-->

${TOOL_RESULT_MCP_HOOK_DETAILS_LEFT_OUT_VAR_0??TOOL_RESULT_MCP_HOOK_DETAILS_LEFT_OUT_VAR_1.other} Details are left out of this message, since the MCP server may have written them. To see them, start Claude Code with --debug and try again: they go to its debug log.
