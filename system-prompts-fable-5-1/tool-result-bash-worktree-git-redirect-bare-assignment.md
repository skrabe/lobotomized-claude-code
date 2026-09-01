<!--
name: 'Tool Result: Worktree git bare-assignment redirect'
description: >-
  Deny-reason fragment when a bare env assignment (GIT_DIR/HOME/etc.) redirects
  a worktree-isolated git command to an unverifiable repository.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_BARE_ASSIGNMENT_VAR_0
-->
assigns ${TOOL_RESULT_BASH_WORKTREE_GIT_REDIRECT_BARE_ASSIGNMENT_VAR_0}, which redirects git to a repository this guard cannot verify
