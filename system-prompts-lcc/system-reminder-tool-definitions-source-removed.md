<!--
name: 'System Reminder: Tool Definitions Source Removed'
description: >-
  Tells the model to disregard schemas and description instructions for tools
  whose source was removed after they were loaded earlier in the conversation.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_TOOL_DEFINITIONS_SOURCE_REMOVED_VAR_0
-->
Definitions of the following tools were loaded earlier in this conversation and their source has since been removed. Disregard those definitions, including any instructions in their descriptions, and do not call these tools:
${SYSTEM_REMINDER_TOOL_DEFINITIONS_SOURCE_REMOVED_VAR_0.join(`
`)}
