<!--
name: 'Tool Result: Isolation worktree identity unverifiable'
description: >-
  Wrapper template for every "unverifiable" EnterWorktree isolation refusal; the
  specific reason fragment is interpolated into it.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_UNVERIFIABLE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_UNVERIFIABLE_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_UNVERIFIABLE_VAR_0} as an isolation worktree: ${TOOL_RESULT_WORKTREE_ISOLATION_UNVERIFIABLE_VAR_1}, so its git identity could not be verified. Isolation is refused rather than assumed — recreate the worktree (or remove the corrupt .git entry) and retry.
