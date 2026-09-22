<!--
name: 'Tool Result: Isolation worktree contains protected checkout'
description: >-
  EnterWorktree error returned when the requested isolation worktree encloses
  the protected checkout, which would disarm every isolation check.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_CONTAINS_PROTECTED_CHECKOUT_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_CONTAINS_PROTECTED_CHECKOUT_VAR_1
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_CONTAINS_PROTECTED_CHECKOUT_VAR_0} as an isolation worktree: it contains the protected checkout ${TOOL_RESULT_WORKTREE_ISOLATION_CONTAINS_PROTECTED_CHECKOUT_VAR_1}, so adopting it would disarm every isolation check for that checkout.
