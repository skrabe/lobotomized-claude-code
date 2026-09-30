<!--
name: 'System Reminder: Subagent handback report via tool'
description: >-
  Instructs a subagent that only a SubagentHandback tool call delivers its final
  report to the caller, and that the call ends its run
ccVersion: 2.1.285
variables:
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_0
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1
-->
${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_0}: when your work is complete, call ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1}({message: <your full report>}). The call ends your run, so make it your last step. Only a ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_REPORT_VIA_TOOL_VAR_1} call reaches your caller as your result; plain text you write at the end is not delivered.
