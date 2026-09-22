<!--
name: 'Tool Result: Isolation worktree shares the protected git dir'
description: >-
  EnterWorktree error returned when the candidate worktree's git directory is
  the shared checkout's own, so git commands there would move the protected
  checkout's refs.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_SHARED_GIT_DIR_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_SHARED_GIT_DIR_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_SHARED_GIT_DIR_VAR_0} as an isolation worktree: its git directory is the shared checkout's own (${TOOL_RESULT_WORKTREE_ISOLATION_SHARED_GIT_DIR_VAR_1.gitDir}), so git commands there move the protected checkout's branches and refs. This usually means the worktree's .git file is stale or was rewritten — recreate the worktree, then retry.
