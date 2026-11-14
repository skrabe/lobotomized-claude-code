<!--
name: 'Tool result: Worktree create unexpected commondir file kept'
description: >-
  Worktree creation error when the unexpected commondir file could not be safely
  deleted, telling not to run git and how to clean up
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_WORKTREE_CREATE_UNEXPECTED_COMMONDIR_FILE_KEPT_VAR_0
-->
${TOOL_RESULT_WORKTREE_CREATE_UNEXPECTED_COMMONDIR_FILE_KEPT_VAR_0} It can make git here fail or load config and hooks from a folder it names, and Claude Code could not safely delete it. Don't run git here yet. Before you try again, read the file, check any folder it names for config or hooks you didn't write, then delete the file.
