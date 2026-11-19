<!--
name: MCP server refused by its plugin
description: >-
  Error thrown when a plugin refuses an MCP server call; the plugin's custom
  refusal or the general retry guidance becomes the tool_result.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MCP_SERVER_REFUSED_BY_PLUGIN_VAR_0
  - TOOL_RESULT_MCP_SERVER_REFUSED_BY_PLUGIN_VAR_1
-->
MCP server "${TOOL_RESULT_MCP_SERVER_REFUSED_BY_PLUGIN_VAR_0}" was not called: ${TOOL_RESULT_MCP_SERVER_REFUSED_BY_PLUGIN_VAR_1??"the plugin that provides it refused this call. Try the call once more. If it is refused again, the plugin has turned the server off."}
