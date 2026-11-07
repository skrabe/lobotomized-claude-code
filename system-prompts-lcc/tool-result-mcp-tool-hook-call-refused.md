<!--
name: 'Tool Result: mcp_tool hook call refused'
description: >-
  Blocking hook error saying an mcp_tool hook's call was refused, with the
  reason words and a remedy
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_TOOL_HOOK_CALL_REFUSED_VAR_0
-->
An mcp_tool hook's call was refused. ${TOOL_RESULT_MCP_TOOL_HOOK_CALL_REFUSED_VAR_0.words} ${TOOL_RESULT_MCP_TOOL_HOOK_CALL_REFUSED_VAR_0.kind==="cannot_tell"?"If this keeps happening, remove this mcp_tool hook or point it at a tool that is not a claude.ai connector's.":"Remove this mcp_tool hook, point it at another tool, or leave that argument out of its input."}
