<!--
name: 'Tool Result: Isolation worktree has symlinked ref storage'
description: >-
  EnterWorktree error returned when the candidate worktree's git metadata
  replaces ref storage with symlinks that alias another repository's refs.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_SYMLINKED_REF_STORE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_SYMLINKED_REF_STORE_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_SYMLINKED_REF_STORE_VAR_0} as an isolation worktree: its git metadata has symbolic links in place of ${TOOL_RESULT_WORKTREE_ISOLATION_SYMLINKED_REF_STORE_VAR_1.symlinkedRefStore.join(", ")}, which aliases another repository's refs into this tree. Recreate the worktree with git worktree add, then retry.
