<!--
name: 'Slash Command: Exit worktree kept, downloads unchecked'
description: >-
  Exit-worktree outcome when the worktree was kept because its
  connector-downloads folder could not be checked.
ccVersion: 2.1.319
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_UNCHECKED_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_UNCHECKED_VAR_1
-->
Worktree kept at ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_UNCHECKED_VAR_0}: Claude Code could not check its ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_UNCHECKED_VAR_1} folder, which may hold files saved from connectors. Check it, then remove the worktree.
