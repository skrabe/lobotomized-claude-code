<!--
name: 'System Reminder: Tool runs on linked computer, not cloud'
description: >-
  Note in ToolSearch reminders that a tool runs on the user's linked computer
  rather than the cloud workspace where other tools run.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_0
  - SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_1
  - SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_2
  - SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_3
-->
${SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_0.length===1?"It":SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_1(SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_2)} runs on the user's linked computer, not in the cloud workspace, where ${SYSTEM_REMINDER_TOOL_RUNS_ON_LINKED_COMPUTER_NOT_CLOUD_VAR_3} runs.
