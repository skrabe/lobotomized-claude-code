<!--
name: Redispatched Orphaned Agent Reminder
description: >-
  Explains a missing completion record after follow-up dispatch and how to
  recover its report.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0
  - SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_1
  - SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_2
-->
No completion record was found for it after it was ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.canContinueAgent?`re-dispatched via ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_1}`:"sent a follow-up message"} in the previous session. It may have been stopped (via the UI, an SDK interrupt, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.canContinueAgent?SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.isWebFetchLaunch?`Send it another message with ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_1} to resume it and get its report before assuming the fetch landed.`:SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.canReadOutputFile?`Send it another message with ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_1} to resume it, or check its worktree/output for partial work before assuming the task landed.`:`Send it another message with ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_1} to resume it and ask for a status report before assuming the task landed.`:SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_2}
