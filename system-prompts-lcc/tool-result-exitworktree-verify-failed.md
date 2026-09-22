<!--
name: ExitWorktree verify failed
description: >-
  ExitWorktree error returned to the model when it cannot verify worktree state
  before removal.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_EXITWORKTREE_VERIFY_FAILED_VAR_0
-->
Could not verify worktree state at ${TOOL_RESULT_EXITWORKTREE_VERIFY_FAILED_VAR_0.worktreePath}. Refusing to remove without explicit confirmation. Re-invoke with discard_changes: true to proceed — or use action: "keep" to preserve the worktree.
