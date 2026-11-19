<!--
name: 'System Reminder: Session context'
description: >-
  Provides selected session context values, marks replacement updates, and
  directs the agent to use them only when highly relevant
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_SESSION_CONTEXT_VAR_0
  - SYSTEM_REMINDER_SESSION_CONTEXT_VAR_1
  - SYSTEM_REMINDER_SESSION_CONTEXT_VAR_2
-->
${SYSTEM_REMINDER_SESSION_CONTEXT_VAR_0}
${SYSTEM_REMINDER_SESSION_CONTEXT_VAR_1.join(`
`)}${SYSTEM_REMINDER_SESSION_CONTEXT_VAR_2}
