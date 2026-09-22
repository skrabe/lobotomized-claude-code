<!--
name: 'Tool Result: MCP servers blocked by managed policy'
description: >-
  tool-result note telling the model the listed MCP servers are blocked by the
  org's managed policy (administrative block, retrying won't help)
ccVersion: 2.1.205
variables:
  - TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_0
  - TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_1
  - TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_2
-->
${TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_0.endsWith(".")?"":"."} Note: these configured MCP servers are blocked by the organization's managed policy, so their tools are unavailable: ${TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_1}${TOOL_RESULT_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_2}. This is an administrative block, not a connection failure — retrying will not help; an administrator manages this setting.
