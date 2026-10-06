<!--
name: 'Tool result: MCP Unicode sanitization max iterations'
description: >-
  Error thrown by the Unicode sanitizer (npo via QE) when sanitizing MCP
  resource/tool data fails to converge; surfaces as the error tool_result of the
  MCP resource-directory listing tool.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_MCP_UNICODE_SANITIZATION_MAX_ITERATIONS_VAR_0
  - TOOL_RESULT_MCP_UNICODE_SANITIZATION_MAX_ITERATIONS_VAR_1
-->
Unicode sanitization reached maximum iterations (${TOOL_RESULT_MCP_UNICODE_SANITIZATION_MAX_ITERATIONS_VAR_0}) for input: ${TOOL_RESULT_MCP_UNICODE_SANITIZATION_MAX_ITERATIONS_VAR_1.slice(0,100)}
