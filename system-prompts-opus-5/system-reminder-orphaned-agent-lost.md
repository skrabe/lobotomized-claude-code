<!--
name: Orphaned background agent (state lost) notice
description: >-
  Notification injected on resume about a background agent that was running at
  exit and lost its in-process state.
ccVersion: 2.1.268
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0
-->
It was running when the previous Claude Code process exited and did not complete. Its in-process state was lost. ${SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0.isWebFetchLaunch?"Launch it again if its report is still needed.":SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0.canReadOutputFile?"Check its worktree/output for partial work before assuming the task landed.":"Do not assume the task landed; launch it again if its result is still needed."}
