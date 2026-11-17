<!--
name: 'Tool Result: Plugin Registered Tool Missing Call Hook'
description: >-
  MCP isError result when a plugin registered a tool but no tool.run hook
  answered the CallTool request.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_0
  - TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1
  - TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_2
-->
${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_0} registered the tool ${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1.params.name} but no hook answered this call: add on("tool.run", { tool: "mcp__${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_2}__${TOOL_RESULT_PLUGIN_REGISTERED_TOOL_MISSING_CALL_HOOK_VAR_1.params.name}" }, ($, e) => ({ result: ... })) to the plugin.
