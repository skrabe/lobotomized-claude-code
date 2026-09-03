<!--
name: 'Tool Result: Bash Worktree Isolation Feeds Assembled Input'
description: >-
  Worktree-isolation refusal when a command feeds input assembled by the
  pipeline that an unknown program may run.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_FEEDS_ASSEMBLED_INPUT_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_FEEDS_ASSEMBLED_INPUT_VAR_1
-->
feeds ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_FEEDS_ASSEMBLED_INPUT_VAR_0} input assembled by the command ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_FEEDS_ASSEMBLED_INPUT_VAR_1}; a program this guard does not know may run that input, so it cannot be shown not to run git
