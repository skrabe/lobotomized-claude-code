<!--
name: 'Tool Result: Worktree resume started from non-git directory'
description: >-
  EnterWorktree/resume error returned when the resume was launched from a
  non-git directory so the worktree cannot be confirmed as a separate isolation
  tree.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_RESUME_FROM_NON_GIT_DIR_VAR_0
-->
This resume was started from inside ${TOOL_RESULT_WORKTREE_ISOLATION_RESUME_FROM_NON_GIT_DIR_VAR_0}, a non-git directory — nothing can confirm it as a separate isolation tree from there. Run the resume from the project checkout instead.
