<!--
name: Orphaned background agent (resumable) notice
description: >-
  Notification injected into model context on resume about a
  stopped-or-interrupted background agent whose transcript is resumable.
ccVersion: 2.1.232
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_RESUMABLE_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENT_RESUMABLE_VAR_1
-->
No completion record was found for background agent "${SYSTEM_REMINDER_ORPHANED_AGENT_RESUMABLE_VAR_0(SYSTEM_REMINDER_ORPHANED_AGENT_RESUMABLE_VAR_1.description)}" from the previous session. It may have been stopped, or it may have been running when the previous Claude Code process exited — either way its transcript is saved on disk, so its progress is not lost. ${SYSTEM_REMINDER_ORPHANED_AGENT_RESUMABLE_VAR_1.isWebFetchLaunch?"Resume it by sending it a message with SendMessage to get its report.":"Resume it by sending it a message with SendMessage, or check its worktree/output for partial work before assuming the task landed."}
