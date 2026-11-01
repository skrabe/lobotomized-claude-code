<!--
name: 'Tool result: worktree guard unset name assigned shell-rewritten value'
description: >-
  Worktree guard reason that an unset variable's inherited text is read as names
  and the command assigns a shell-rewritten name.
ccVersion: 2.1.316
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_2
  - TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_3
-->
${TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_1)}; ${TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_2} is never set in this command, so the shell reads the text ${TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_2} inherits as more variable names, and this command assigns the value ${TOOL_RESULT_BASH_WORKTREE_GUARD_UNSET_NAME_SHELL_REWRITES_VAR_3}, a name the shell itself rewrites as commands run; run the arithmetic as a separate Bash command without that assignment
