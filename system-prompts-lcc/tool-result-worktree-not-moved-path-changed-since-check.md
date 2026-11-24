<!--
name: 'Tool result: worktree path changed since permission check'
description: >-
  Refusal when the worktree path now leads elsewhere than at permission check
  time; asks to call the tool again.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_0
  - TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_1
  - TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_2
  - TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_3
-->
The ${TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_0} was not moved: ${TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_1(TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_2)} now leads to a different folder than when its permission check ran. Call ${TOOL_RESULT_WORKTREE_NOT_MOVED_PATH_CHANGED_SINCE_CHECK_VAR_3} again to have it checked anew, and tell the user if this happens again.
