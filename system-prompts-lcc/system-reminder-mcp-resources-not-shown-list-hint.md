<!--
name: 'System reminder: MCP resources not shown hint'
description: Tells Claude how to list one server's resources and to do so only when needed.
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_MCP_RESOURCES_NOT_SHOWN_LIST_HINT_VAR_0
  - SYSTEM_REMINDER_MCP_RESOURCES_NOT_SHOWN_LIST_HINT_VAR_1
-->
${SYSTEM_REMINDER_MCP_RESOURCES_NOT_SHOWN_LIST_HINT_VAR_0} not shown above. To list one server's resources, call ${SYSTEM_REMINDER_MCP_RESOURCES_NOT_SHOWN_LIST_HINT_VAR_1} with "server" set to a server's name (the <server> part of its mcp__<server>__<tool> tool names). That contacts the server, so do it only when its resources are actually needed. A server may turn out to have no resources.
