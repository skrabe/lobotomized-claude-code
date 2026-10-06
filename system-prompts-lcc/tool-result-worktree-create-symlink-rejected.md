<!--
name: 'Tool result: worktree create symlink rejected'
description: 'Error when .claude, .claude/worktrees or the worktree path is a symlink.'
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_1
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_2
-->
Cannot create worktree: ${TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0(TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_1,TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_2)} is a symlink. A repository-committed symlink at .claude, .claude/worktrees, or .claude/worktrees/<name> could redirect worktree creation outside the repository. Remove the symlink and retry.
