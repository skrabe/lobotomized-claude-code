<!--
name: 'System Reminder: Task status ask agent for result'
description: >-
  Clause telling Claude to message the agent for its result if it cannot read
  the output file
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_TASK_STATUS_ASK_AGENT_FOR_RESULT_VAR_0
  - SYSTEM_REMINDER_TASK_STATUS_ASK_AGENT_FOR_RESULT_VAR_1
-->
 (if you cannot read it and do not already have its result, ask agent ${SYSTEM_REMINDER_TASK_STATUS_ASK_AGENT_FOR_RESULT_VAR_0} with ${SYSTEM_REMINDER_TASK_STATUS_ASK_AGENT_FOR_RESULT_VAR_1})
