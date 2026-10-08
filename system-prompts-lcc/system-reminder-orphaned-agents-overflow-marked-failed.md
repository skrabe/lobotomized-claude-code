<!--
name: Orphaned tasks overflow marked failed
description: >-
  Explains that excess orphaned background tasks lost state and were marked
  failed.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENTS_OVERFLOW_MARKED_FAILED_VAR_0
-->
They were running when the previous Claude Code process exited and did not complete; their in-process state was lost.${SYSTEM_REMINDER_ORPHANED_AGENTS_OVERFLOW_MARKED_FAILED_VAR_0()?"":" Check each worktree/output for partial work before assuming a task landed."} They have been marked failed.
