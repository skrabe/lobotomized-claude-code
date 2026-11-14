<!--
name: 'System reminder: MCP servers refused by network proxy'
description: >-
  Tells the model configured MCP servers are refused by the session network
  proxy policy
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_REFUSED_NETWORK_PROXY_VAR_0
  - SYSTEM_REMINDER_MCP_SERVERS_REFUSED_NETWORK_PROXY_VAR_1
-->
The following MCP servers are configured, but this session's network proxy refuses them by policy. Their tools are unavailable for this session:
${SYSTEM_REMINDER_MCP_SERVERS_REFUSED_NETWORK_PROXY_VAR_0}${SYSTEM_REMINDER_MCP_SERVERS_REFUSED_NETWORK_PROXY_VAR_1}

This is not a sign-in problem or a connection failure: authorizing or retrying will not help. If the user's request depends on one of these servers, tell them it is not available from this session.
