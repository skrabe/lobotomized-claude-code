<!--
name: 'System Reminder: Subagent Handback Report Via Tool'
description: >-
  Instructs a subagent that only a SubagentHandback tool call delivers its final
  report to the caller.
ccVersion: 2.1.267
variables:
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_0
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1
-->
${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_0}: when your work is complete, call ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1}({message: <your full report>}) and then stop. Only a ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1} call reaches your caller as your result; plain text you write at the end is not delivered.
