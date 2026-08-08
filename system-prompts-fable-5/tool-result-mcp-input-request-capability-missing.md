<!--
name: MCP Input Request Capability Missing
description: >-
  Error text returned via yFs() — which for tools/call builds
  {content:[{type:'text',text}],isError:true} — telling the calling model that a
  server-initiated input request (elicitation/sampling/roots) cannot be made
  because the 2025-era client did not declare the required capability.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_0
  - TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_1
  - TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_2
-->

Cannot request input '${TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_0}' (${TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_1.method}): the client on this 2025-era connection did not declare the required capability${TOOL_RESULT_MCP_INPUT_REQUEST_CAPABILITY_MISSING_VAR_2===void 0?" (no client capabilities are available on this connection — per-request legacy serving cannot receive server-to-client requests)":""}
