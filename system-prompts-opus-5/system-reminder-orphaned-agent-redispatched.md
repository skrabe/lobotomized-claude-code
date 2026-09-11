<!--
name: Orphaned background agent (re-dispatched) notice
description: >-
  Notification injected into model context on resume when a re-dispatched
  background agent has no completion record.
ccVersion: 2.1.268
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0
-->
No completion record was found for it after it was re-dispatched via SendMessage in the previous session. It may have been stopped (via the UI, an SDK interrupt, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. ${SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.isWebFetchLaunch?"Send it another message with SendMessage to resume it and get its report before assuming the fetch landed.":SYSTEM_REMINDER_ORPHANED_AGENT_REDISPATCHED_VAR_0.canReadOutputFile?"Check its worktree/output for partial work before assuming the task landed.":"Send it another message with SendMessage to resume it and ask for a status report before assuming the task landed."}
