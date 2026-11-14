<!--
name: 'Tool Result: Plugin path leads into MCPB cache'
description: >-
  Reason telling that a plugin path leads into the .mcpb-cache folder that
  Claude Code may overwrite when unpacking MCP bundles, so the plugin author
  must move it
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PLUGIN_PATH_LEADS_INTO_MCPB_CACHE_VAR_0
-->
it leads into ${TOOL_RESULT_PLUGIN_PATH_LEADS_INTO_MCPB_CACHE_VAR_0}, which Claude Code may have overwritten when it unpacked the plugin's MCP bundles; the plugin's author needs to move it to another folder
