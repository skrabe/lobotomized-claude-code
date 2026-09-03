<!--
name: 'Tool Result: Plugin Registered Tool Missing Call Hook'
description: >-
  MCP isError result when a plugin registered a tool but no tool.call hook
  answered the CallTool request.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_0
  - TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1
-->
${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_0} registered the tool ${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1.params.name} but no tool.call hook answered this call: add on("tool.call", { tool: "mcp__${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_0}__${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1.params.name}" }, ($, e) => ({ result: ... })) to the plugin.
