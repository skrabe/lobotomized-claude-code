<!--
name: 'Tool Result: MCP servers refused by network proxy'
description: >-
  ToolSearch no-match result note that the session's network proxy refuses
  configured MCP servers by policy, so authorizing or retrying won't help.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_0
  - TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_1
  - TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_2
-->
${TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_0.endsWith(".")?"":"."} Note: this session's network proxy refuses these configured MCP servers by policy, so their tools are unavailable: ${TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_1}${TOOL_RESULT_MCP_SERVERS_REFUSED_BY_NETWORK_PROXY_VAR_2}. This is not a sign-in problem or a connection failure, so authorizing or retrying will not help.
