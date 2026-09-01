<!--
name: 'Tool Result: Worktree Containment Check Failed'
description: >-
  WorktreeIsolationError message emitted when the created worktree resolves
  outside the expected .claude/worktrees location; returned to the model as a
  tool error.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_0
  - TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_1
  - TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_2
-->
Cannot create worktree: ${TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_0} resolved to ${TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_1}, which is not the expected worktree location ${TOOL_RESULT_WORKTREE_CREATE_CONTAINMENT_FAILED_VAR_2}.
