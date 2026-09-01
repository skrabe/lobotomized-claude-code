<!--
name: 'Tool Result: Worktree git guard — wrapper command before git'
description: >-
  Refusal clause: a wrapper command runs before git whose string payload can't
  be verified to leave the worktree alone.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_WRAPPER_BEFORE_GIT_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GIT_WRAPPER_BEFORE_GIT_VAR_1
-->
runs ${TOOL_RESULT_BASH_WORKTREE_GIT_WRAPPER_BEFORE_GIT_VAR_0(TOOL_RESULT_BASH_WORKTREE_GIT_WRAPPER_BEFORE_GIT_VAR_1)} before a git command, whose string payload can't be verified to leave the worktree alone
