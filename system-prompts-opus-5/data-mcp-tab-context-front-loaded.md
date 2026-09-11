<!--
name: 'Data: MCP Tab Context Front Loaded'
description: >-
  Front-loaded tabs_context_mcp JSON plus tab-cleanup guidance appended onto the
  MCP tool result the model reads.
ccVersion: 2.1.268
variables:
  - DATA_MCP_TAB_CONTEXT_FRONT_LOADED_VAR_0
-->

Tab context (from front-loaded tabs_context_mcp):
${DATA_MCP_TAB_CONTEXT_FRONT_LOADED_VAR_0.tabContextJson}
Tabs in this group were opened for this task and are yours to clean up: close each with tabs_close_mcp once you no longer need it and before finishing, unless the user asked to see it or wants it kept open.
