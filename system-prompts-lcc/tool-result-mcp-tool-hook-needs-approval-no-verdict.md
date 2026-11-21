<!--
name: 'Tool Result: MCP tool hook needs approval, no verdict'
description: >-
  Explains a PreToolUse mcp_tool hook gave no verdict because the MCP tool needs
  a person's approval that a hook call cannot request
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_TOOL_HOOK_NEEDS_APPROVAL_NO_VERDICT_VAR_0
-->
MCP tool "${TOOL_RESULT_MCP_TOOL_HOOK_NEEDS_APPROVAL_NO_VERDICT_VAR_0.tool}" on server "${TOOL_RESULT_MCP_TOOL_HOOK_NEEDS_APPROVAL_NO_VERDICT_VAR_0.server}" needs a person's approval, which a hook's call can't ask for, so this hook gave no verdict. Where that tool can be set to always allow, that lets the hook run
