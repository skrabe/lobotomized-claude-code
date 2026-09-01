<!--
name: 'System Reminder: Undiscovered tool schemas'
description: >-
  Reminder that some available tools' schemas are not yet loaded and to use
  ToolSearch before concluding a capability is missing.
ccVersion: 2.1.178
variables:
  - SYSTEM_REMINDER_UNDISCOVERED_TOOL_SCHEMAS_VAR_0
  - SYSTEM_REMINDER_UNDISCOVERED_TOOL_SCHEMAS_VAR_1
-->
Some available tools' schemas are not loaded yet: ${SYSTEM_REMINDER_UNDISCOVERED_TOOL_SCHEMAS_VAR_0}. Before concluding a capability is missing or building a workaround, use ${SYSTEM_REMINDER_UNDISCOVERED_TOOL_SCHEMAS_VAR_1} to find and load relevant tools — keywords to search, or query "select:<name>[,<name>...]" for specific tools. Calling a tool before its schema is loaded will fail.
