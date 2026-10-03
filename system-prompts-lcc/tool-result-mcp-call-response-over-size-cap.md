<!--
name: 'Tool Result: mcp_call MCP response over size cap'
description: >-
  Error result for an mcp_call whose MCP server response exceeded Claude Code's
  byte cap: no result returned, the tool may have run, check the effect before
  retrying and request a smaller result
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_0
  - TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_1
  - TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_2
-->
MCP server ${TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_0} sent a response over Claude Code's ${TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_1.round(TOOL_RESULT_MCP_CALL_RESPONSE_OVER_SIZE_CAP_VAR_2.capBytes/1024/1024)} MB limit, so this mcp_call got no result. The server may have run the tool, so check whether the call took effect before retrying mcp_call, and ask the tool for a smaller result if you retry.
