<!--
name: 'Tool Result: Bash Worktree Guard Unlocated Program'
description: >-
  Worktree-guard denial when a computed argument sits where the program operand
  cannot be located.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_2
-->
with ${TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_0??`${TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_1(TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_UNLOCATED_PROGRAM_VAR_2[ve].value)} (a computed argument goes after the script or --)`} where it cannot tell which operand is the program, next to an operand or input computed at runtime
