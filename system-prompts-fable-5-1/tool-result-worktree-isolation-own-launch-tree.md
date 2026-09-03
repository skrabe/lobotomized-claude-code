<!--
name: 'Tool Result: Isolation worktree is the launch checkout'
description: >-
  EnterWorktree error returned when the requested worktree is the checkout this
  session launched from, so an honest and a forged record are indistinguishable.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_OWN_LAUNCH_TREE_VAR_0
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_OWN_LAUNCH_TREE_VAR_0} as an isolation worktree: it is the checkout this session launched from. An honest launch-from-inside and a forged record are indistinguishable here, so both are refused — launch from the parent checkout to enter or resume this worktree.
