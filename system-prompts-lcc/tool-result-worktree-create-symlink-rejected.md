<!--
name: 'Tool Result: Worktree create symlink rejected'
description: >-
  Error when a repository-committed symlink in the .claude/worktrees path would
  redirect worktree creation.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_1
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_2
-->
Cannot create worktree: ${TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0(TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_1.anchor,TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_2)} is a symlink. A repository-committed symlink at .claude, .claude/worktrees, or .claude/worktrees/<name> could redirect worktree creation outside the repository. Remove the symlink and retry.
