<!--
name: 'Slash Command: Exit worktree kept, downloads hold files'
description: >-
  Exit-worktree outcome when the worktree was kept because its
  connector-downloads folder now holds saved files.
ccVersion: 2.1.319
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_HOLD_FILES_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_HOLD_FILES_VAR_1
-->
Worktree kept at ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_HOLD_FILES_VAR_0}: its ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_DOWNLOADS_HOLD_FILES_VAR_1} folder now holds files saved from connectors. Move them out, then remove the worktree.
