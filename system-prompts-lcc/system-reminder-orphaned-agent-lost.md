<!--
name: Orphaned background agent (state lost) notice
description: >-
  Notification injected on resume about a background agent that was running at
  exit and lost its in-process state.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0
-->
It was running when the previous Claude Code process exited and did not complete. Its in-process state was lost. ${SYSTEM_REMINDER_ORPHANED_AGENT_LOST_VAR_0}
