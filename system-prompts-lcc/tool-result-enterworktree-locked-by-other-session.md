<!--
name: 'Tool result: EnterWorktree locked by another session'
description: >-
  EnterWorktree error when another running Claude Code session holds the
  worktree lock.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ENTERWORKTREE_LOCKED_BY_OTHER_SESSION_VAR_0
  - TOOL_RESULT_ENTERWORKTREE_LOCKED_BY_OTHER_SESSION_VAR_1
-->
Cannot enter worktree: ${TOOL_RESULT_ENTERWORKTREE_LOCKED_BY_OTHER_SESSION_VAR_0} belongs to another running Claude Code session (locked: ${TOOL_RESULT_ENTERWORKTREE_LOCKED_BY_OTHER_SESSION_VAR_1.lockReason}). Wait for that session to finish or choose a different worktree.
