<!--
name: 'Tool Result: ToolSearch MCP servers tool listing failed'
description: >-
  Note appended to an empty ToolSearch result naming connected MCP servers whose
  tool listing failed, telling the model not to conclude they have no tools.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_0
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_1
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_2
-->
${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_0.endsWith(".")?"":"."} Note: these MCP servers are connected, but listing their tools failed, so their tools are unavailable for now: ${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_1}${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_2}. Treat this as a failure to load their tools — do not conclude the server has no tools.
