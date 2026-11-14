<!--
name: 'Tool whenToUse: MCP connector search'
description: >-
  Deferred-tool listing line telling Claude to search for MCP connectors when a
  task needs an unreachable outside service.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_CONNECTOR_SEARCH_VAR_0
-->
When the task needs an outside product or service that none of your tools reach, whether or not the user named one, use it to find MCP connectors; it connects nothing itself, and ${TOOL_WHEN_TO_USE_CONNECTOR_SEARCH_VAR_0} takes its results.
