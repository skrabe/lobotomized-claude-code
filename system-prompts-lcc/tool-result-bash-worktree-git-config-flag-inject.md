<!--
name: 'Tool Result: Worktree git guard — git -c config injection'
description: >-
  Refusal clause: an opaque -c/config value is passed to git, injecting
  configuration whose write target can't be verified.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_CONFIG_FLAG_INJECT_VAR_0
-->
passes ${TOOL_RESULT_BASH_WORKTREE_GIT_CONFIG_FLAG_INJECT_VAR_0.opaque} to git, injecting configuration whose effect on where git writes can't be verified
