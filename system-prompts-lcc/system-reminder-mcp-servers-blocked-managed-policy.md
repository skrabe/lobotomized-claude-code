<!--
name: 'System Reminder: MCP servers blocked by managed policy'
description: >-
  System-reminder context listing MCP servers blocked by the org's managed
  policy — their tools are unavailable this session; an administrative block
ccVersion: 2.1.205
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_0
  - SYSTEM_REMINDER_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_1
-->
The following MCP servers are configured but blocked by the organization's managed policy — their tools are unavailable for this session:
${SYSTEM_REMINDER_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_0}${SYSTEM_REMINDER_MCP_SERVERS_BLOCKED_MANAGED_POLICY_VAR_1}

This is an administrative block, not a connection failure: retrying will not help. If the user's request depends on one of these servers, tell them it is disabled by policy and that an administrator manages this setting.
