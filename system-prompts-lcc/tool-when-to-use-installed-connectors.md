<!--
name: 'Tool whenToUse: Installed MCP connectors'
description: >-
  Deferred-tool listing line telling Claude to list the user's installed
  connectors, and to use search then details for recommendations.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_INSTALLED_CONNECTORS_VAR_0
  - TOOL_WHEN_TO_USE_INSTALLED_CONNECTORS_VAR_1
-->
When the user asks which claude.ai MCP connectors they already have, or whether one is connected or its tools are available in this session, use it; to recommend connectors they do not have yet, use ${TOOL_WHEN_TO_USE_INSTALLED_CONNECTORS_VAR_0} then ${TOOL_WHEN_TO_USE_INSTALLED_CONNECTORS_VAR_1}.
