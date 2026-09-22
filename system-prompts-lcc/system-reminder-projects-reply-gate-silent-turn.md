<!--
name: 'System Reminder: Projects reply gate silent turn'
description: >-
  Tells the model a turn without a terminal project MCP tool call delivered
  nothing to the project thread, and which tools to call now.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_0
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_1
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_2
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_3
  - SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_4
-->
${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_0} Your last turn ended without a terminal \`mcp__${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_1}__*\` tool call, so nothing reached the project thread: plain text is not delivered there. Call \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_2}\` now with what the thread should see, \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_3}\` if you dispatched work that reports back later, or \`${SYSTEM_REMINDER_PROJECTS_REPLY_GATE_SILENT_TURN_VAR_4}\` if no reply is warranted.
