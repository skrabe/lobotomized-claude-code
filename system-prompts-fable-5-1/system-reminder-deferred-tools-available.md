<!--
name: 'System Reminder: Deferred tools available'
description: >-
  Announces newly available deferred tools and instructs the agent to load their
  schemas through ToolSearch
ccVersion: 2.1.257
variables:
  - TOOL_SEARCH_TOOL_NAME
-->
The following deferred tools are now available via ${TOOL_SEARCH_TOOL_NAME}. Their schemas are NOT loaded — calling them directly will fail with InputValidationError. Use ${TOOL_SEARCH_TOOL_NAME} with query "select:<name>[,<name>...]" to load tool schemas before calling them:
