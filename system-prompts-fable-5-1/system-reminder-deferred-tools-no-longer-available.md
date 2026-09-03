<!--
name: 'System Reminder: Deferred Tools No Longer Available In Session'
description: >-
  Tells the model non-MCP deferred tools announced earlier are gone and
  ToolSearch will not match them.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_NO_LONGER_AVAILABLE_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_NO_LONGER_AVAILABLE_VAR_1
-->
The following deferred tools are no longer available in this session. Do not search for them — ${SYSTEM_REMINDER_DEFERRED_TOOLS_NO_LONGER_AVAILABLE_VAR_0} will return no match:
${SYSTEM_REMINDER_DEFERRED_TOOLS_NO_LONGER_AVAILABLE_VAR_1.other.join(`
`)}
