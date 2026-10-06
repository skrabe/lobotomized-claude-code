<!--
name: 'Tool result: EnterWorktree not registered'
description: >-
  EnterWorktree error when the path is not a registered git worktree, with a
  hint to list worktrees.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ENTERWORKTREE_NOT_REGISTERED_WORKTREE_VAR_0
  - TOOL_RESULT_ENTERWORKTREE_NOT_REGISTERED_WORKTREE_VAR_1
-->
Cannot enter worktree: ${TOOL_RESULT_ENTERWORKTREE_NOT_REGISTERED_WORKTREE_VAR_0} is not a registered worktree of ${TOOL_RESULT_ENTERWORKTREE_NOT_REGISTERED_WORKTREE_VAR_1}. Run 'git -C ${TOOL_RESULT_ENTERWORKTREE_NOT_REGISTERED_WORKTREE_VAR_1} worktree list' to see registered worktrees.
