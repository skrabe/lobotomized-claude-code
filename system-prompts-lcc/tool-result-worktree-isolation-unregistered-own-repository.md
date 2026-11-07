<!--
name: 'Tool Result: Worktree isolation unregistered own repository'
description: >-
  Refusal when the worktree path holds a repository of its own inside a
  checkout's .claude/worktrees
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_3
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_0} as an isolation worktree: it is a repository of its own (a .git directory, not a worktree's .git file) inside ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_1}${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_2}, where only worktrees that the checkout ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_OWN_REPOSITORY_VAR_3} itself made are accepted. If you or a WorktreeCreate hook cloned it there, move the clone somewhere that is not inside any checkout's .claude/worktrees directory. If nobody meant a repository to be here, do not trust it or run git in it.
