<!--
name: 'Tool Result: Worktree Creation Rejected (Symlink)'
description: >-
  WorktreeIsolationError message thrown by the worktree-containment check;
  reaches the model as a <tool_use_error> tool result when EnterWorktree creates
  a worktree.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0
-->
Cannot create worktree: ${TOOL_RESULT_WORKTREE_CREATE_SYMLINK_REJECTED_VAR_0} is a symlink. A repository-committed symlink at .claude, .claude/worktrees, or .claude/worktrees/<name> could redirect worktree creation outside the repository. Remove the symlink and retry.
