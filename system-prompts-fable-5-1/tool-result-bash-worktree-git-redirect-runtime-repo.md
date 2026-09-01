<!--
name: 'Tool Result: Worktree git points at runtime-computed repository'
description: >-
  Deny-reason fragment when a worktree-isolated git command pins a repository
  path computed at runtime that can't be verified.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_REPO_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_REPO_VAR_1
-->
points git at a repository computed at runtime (${TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_REPO_VAR_0} ${TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_RUNTIME_REPO_VAR_1}), which can't be verified before it runs
