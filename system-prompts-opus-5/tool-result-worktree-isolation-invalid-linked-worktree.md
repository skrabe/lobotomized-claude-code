<!--
name: 'Tool Result: Isolation worktree not a registered linked worktree'
description: >-
  EnterWorktree error returned when the candidate uses another repository's refs
  without being a registered worktree of it.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_INVALID_LINKED_WORKTREE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_INVALID_LINKED_WORKTREE_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_INVALID_LINKED_WORKTREE_VAR_0} as an isolation worktree: it uses another repository's refs (${TOOL_RESULT_WORKTREE_ISOLATION_INVALID_LINKED_WORKTREE_VAR_1.commonDir}) without being a registered worktree of it (its admin directory or back-pointer does not check out). Recreate the worktree with git worktree add, then retry.
