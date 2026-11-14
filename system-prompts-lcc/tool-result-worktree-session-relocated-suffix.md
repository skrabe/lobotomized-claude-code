<!--
name: 'Tool result: worktree error session relocated'
description: >-
  Rewrites a worktree tool error to add that the session is no longer where it
  stood and names its new directory
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_0
  - TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_1
  - TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_2
  - TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_3
-->
${TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_0(TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_1).trimEnd().replace(/[^.!?]$/,"$&.")} The session is no longer where it stood: it is now in ${TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_2(TOOL_RESULT_WORKTREE_SESSION_RELOCATED_SUFFIX_VAR_3())}.
