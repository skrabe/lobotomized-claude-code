<!--
name: 'System Reminder: Tool Batching Tip'
description: >-
  Tool-result system reminder telling the model a tool accepts multiple entries
  in one call and that no action is needed for this result.
ccVersion: 2.1.237
variables:
  - SYSTEM_REMINDER_TOOL_BATCHING_TIP_VAR_0
-->
<system-reminder>Tip: ${SYSTEM_REMINDER_TOOL_BATCHING_TIP_VAR_0.name} accepts multiple entries in one call (`${SYSTEM_REMINDER_TOOL_BATCHING_TIP_VAR_0.entryFieldName}: [{...}, {...}]`). No action needed for this result.</system-reminder>
