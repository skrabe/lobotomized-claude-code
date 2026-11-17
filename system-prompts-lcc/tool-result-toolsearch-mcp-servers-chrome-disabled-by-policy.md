<!--
name: 'Tool Result: ToolSearch MCP servers Claude in Chrome disabled by policy'
description: >-
  ToolSearch no-match note: listed MCP servers provide Claude in Chrome,
  disabled by organization policy, so retrying won't help.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_0
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_1
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_2
-->
${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_0.endsWith(".")?"":"."} Note: these configured MCP servers provide Claude in Chrome, which is disabled by the organization's policy, so their tools are unavailable: ${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_1}${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_CHROME_DISABLED_BY_POLICY_VAR_2}. This is not a connection failure, so retrying will not help, and there may be no setting or administrator that can turn it on.
