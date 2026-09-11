<!--
name: Orphaned agents aggregate — stopped
description: >-
  Aggregate system-reminder listing background agents from a previous session
  with no completion record (stopped variant), injected as a task-notification
  into the model context.
ccVersion: 2.1.268
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_COUNT_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_COUNT_VAR_1
-->
No completion record was found for them in the previous session. They may have been stopped, or they may have been running when the previous Claude Code process exited — either way their transcripts are saved, so their progress is not lost. ${SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_COUNT_VAR_0?"Resume any of them by sending a message to its id with SendMessage to get its report.":SYSTEM_REMINDER_ORPHANED_AGENTS_AGGREGATE_STOPPED_COUNT_VAR_1?"Resume any of them by sending a message to its id with SendMessage and ask for a status report before assuming the task landed.":"Resume any of them by sending a message to its id with SendMessage, or check its worktree/output for partial work before assuming the task landed."}
