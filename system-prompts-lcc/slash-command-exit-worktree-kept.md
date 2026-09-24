<!--
name: 'Slash Command: Exit Worktree Kept'
description: >-
  /exit output when the user keeps the worktree on exit: says the worktree was
  kept and gives the path (and branch) where the work is saved.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_VAR_1
-->
Worktree kept. Your work is saved at ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_VAR_0.worktreePath}${SLASH_COMMAND_EXIT_WORKTREE_KEPT_VAR_1}
