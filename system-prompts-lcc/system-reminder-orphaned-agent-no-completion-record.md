<!--
name: Orphaned Agent Without Completion Record
description: >-
  Explains a restored background agent's uncertain completion and available
  resume steps.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_1
  - SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_2
-->
No completion record was found for it in the previous session. It may have been stopped, or it may have been running when the previous Claude Code process exited${SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_0.canContinueAgent?" — either way its transcript is saved, so its progress is not lost":""}. ${SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_0.canContinueAgent?SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_0.isWebFetchLaunch?`Resume it by sending it a message with ${SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_1} to get its report.`:SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_0.canReadOutputFile?`Resume it by sending it a message with ${SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_1}, or check its worktree/output for partial work before assuming the task landed.`:`Resume it by sending it a message with ${SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_1} and ask for a status report before assuming the task landed.`:SYSTEM_REMINDER_ORPHANED_AGENT_NO_COMPLETION_RECORD_VAR_2}
