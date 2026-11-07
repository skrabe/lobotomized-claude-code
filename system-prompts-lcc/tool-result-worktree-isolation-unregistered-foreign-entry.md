<!--
name: 'Tool Result: Worktree isolation unregistered foreign entry'
description: >-
  Refusal when the worktree's .git leads to an entry that is not one of the
  checkout's own worktree entries
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_3
  - TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_4
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_0} as an isolation worktree: ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_1}, and its .git leads to ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_2(TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_3.gitDir,"a directory (its path is not repeated here)")}, which is not one of ${TOOL_RESULT_WORKTREE_ISOLATION_UNREGISTERED_FOREIGN_ENTRY_VAR_4}'s own worktree entries. If this worktree is yours, copy out what you need and recreate it; otherwise do not trust it or run git in it.
