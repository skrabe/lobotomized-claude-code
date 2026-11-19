<!--
name: 'Exit: worktree could not be removed'
description: >-
  Exit dialog result when removing the worktree failed and it was kept, with the
  removal error appended when known.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_REMOVE_FAILED_KEPT_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_REMOVE_FAILED_KEPT_VAR_1
-->
Couldn't remove worktree. Kept at ${SLASH_COMMAND_EXIT_WORKTREE_REMOVE_FAILED_KEPT_VAR_0.worktreePath}${SLASH_COMMAND_EXIT_WORKTREE_REMOVE_FAILED_KEPT_VAR_1===void 0?"":`: ${SLASH_COMMAND_EXIT_WORKTREE_REMOVE_FAILED_KEPT_VAR_1}`}
