<!--
name: 'Tool result: routine create unrequested connectors attached'
description: >-
  RemoteTrigger create result warning that no connectors were requested but the
  routine got the account's connectors, telling the model to tell the user and
  how to clear or narrow mcp_connections.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_ROUTINE_CREATE_UNREQUESTED_CONNECTORS_ATTACHED_VAR_0
-->
⚠ No connectors were asked for (mcp_connections is empty or absent), but this routine has: ${TOOL_RESULT_ROUTINE_CREATE_UNREQUESTED_CONNECTORS_ATTACHED_VAR_0}. The server attaches the account's connected connectors when none are named, and every run of this routine can use them. Tell the user. To remove them, call update on this routine with {"clear_mcp_connections": true}, or with mcp_connections holding only the entries to keep, copied from this response. An empty mcp_connections changes nothing.
