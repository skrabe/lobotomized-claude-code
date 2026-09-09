<!--
name: Orphaned background agent (state lost) notice
description: >-
  Notification injected on resume about a background agent that was running at
  exit and lost its in-process state.
ccVersion: 2.1.265
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0
-->
It was running when the previous Claude Code process exited and did not complete. Its in-process state was lost. ${SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0.isWebFetchLaunch?"Launch it again if its report is still needed.":"Check its worktree/output for partial work before assuming the task landed."}
