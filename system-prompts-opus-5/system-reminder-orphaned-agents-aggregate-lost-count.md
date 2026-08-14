<!--
name: Orphaned agents aggregate — lost
description: >-
  Aggregate system-reminder listing background agents that were running when the
  previous Claude Code process exited and lost in-process state, injected as a
  task-notification into the model context.
ccVersion: 2.1.232
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_1
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_2
-->
${SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_0.length} background agents were running when the previous Claude Code process exited and did not complete: ${SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_1}. Their in-process state was lost. ${SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_LOST_COUNT_VAR_2}
