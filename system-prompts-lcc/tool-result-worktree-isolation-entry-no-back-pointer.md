<!--
name: 'Tool Result: Worktree isolation entry has no back pointer'
description: >-
  Refusal when the worktree's .git leads to an entry that no longer names any
  worktree back
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_3
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_0} as an isolation worktree: its .git leads to ${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_1} that no longer names any worktree back (its gitdir file is missing, unreadable or does not name a .git file).${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_2} ${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NO_BACK_POINTER_VAR_3}
