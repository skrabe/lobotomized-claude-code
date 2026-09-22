<!--
name: 'Tool Result: Worktree resume started from its own repository'
description: >-
  EnterWorktree/resume error returned when the resume ran from inside a
  directory that is its own repository, so it cannot be confirmed as a separate
  isolation worktree.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_RESUME_FROM_OWN_REPO_VAR_0
-->
This resume was started from inside ${TOOL_RESULT_WORKTREE_ISOLATION_RESUME_FROM_OWN_REPO_VAR_0}, which is its own repository — it cannot be confirmed as a separate isolation worktree from there. Run the resume from the project checkout instead.
