<!--
name: 'Tool Result: Isolation worktree resolves elsewhere'
description: >-
  EnterWorktree error returned when git resolves the candidate worktree's
  working tree to a different path (core.worktree redirect or a checkout above
  it).
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_WORK_TREE_ELSEWHERE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_WORK_TREE_ELSEWHERE_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_WORK_TREE_ELSEWHERE_VAR_0} as an isolation worktree: git resolves its working tree to ${TOOL_RESULT_WORKTREE_ISOLATION_WORK_TREE_ELSEWHERE_VAR_1.topLevel} (a core.worktree redirect, or a checkout discovered above it), so commands run there would write outside the worktree. Remove the redirect, restore the worktree's own .git, or recreate the worktree, then retry.
