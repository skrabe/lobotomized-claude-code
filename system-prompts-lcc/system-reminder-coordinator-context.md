<!--
name: 'System Reminder: Coordinator Context'
description: >-
  Wrapper for the coordinator_context attachment: optional worker-tools-changed
  lead, the tools list, and the standard reminder footer.
ccVersion: 2.1.268
variables:
  - SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_0
  - SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_1
  - SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_2
-->
${SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_0===!0?`The worker tools have changed; this replaces the earlier list.

`:""}${SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_1}

${SYSTEM_REMINDER_COORDINATOR_CONTEXT_VAR_2}
