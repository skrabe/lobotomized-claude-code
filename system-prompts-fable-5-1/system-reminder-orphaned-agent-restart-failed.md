<!--
name: Orphaned background agent (restart failed) notice
description: >-
  Notification injected into model context on resume about a background agent
  that could not be automatically restarted.
ccVersion: 2.1.232
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_1
  - SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_2
-->
Background agent "${SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_0(SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_1.description)}" from the previous session could not be automatically restarted: ${SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_0(SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_2)}. Its transcript may still be resumable by sending it a message with SendMessage${SYSTEM_REMINDER_ORPHANED_AGENT_RESTART_FAILED_VAR_1.isWebFetchLaunch?", which is the only way to get its report.":"; check its worktree/output for partial work before assuming the task landed."}
