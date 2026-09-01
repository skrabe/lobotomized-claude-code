<!--
name: 'Tool Result: Worktree git points at runtime-computed directory'
description: >-
  Deny-reason fragment when a worktree-isolated git command uses -C with a
  directory computed at runtime that can't be verified before it runs.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_DIR_VAR_0
-->
points git at a directory computed at runtime (-C ${TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_DIR_VAR_0}), which can't be verified before it runs
