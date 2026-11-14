<!--
name: 'Tool whenToUse: MCP connector details'
description: >-
  Deferred-tool listing line telling Claude to resolve connector details from
  directoryUuid or server_id values and never guess ids.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_CONNECTOR_DETAILS_VAR_0
-->
When you hold directoryUuid values from ${TOOL_WHEN_TO_USE_CONNECTOR_DETAILS_VAR_0}, or server_id values from your system prompt, and are about to describe those connectors to the user, use it for their details and install state; never guess ids or pass names.
