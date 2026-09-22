<!--
name: 'Tool Result: Bash Blocked, Unresolvable Working Directory Spelling'
description: >-
  Bash pre-spawn error telling the model its working directory is spelled
  unresolvably (symlinked dot segment / UNC / device namespace) and to re-run
  from the worktree's direct symlink-free path.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WORKTREE_CWD_UNRESOLVABLE_SPELLING_VAR_0
-->
This command was blocked because its working directory is spelled in a form that cannot be safely resolved (for example through a symlink storing a raw dot segment, a network-share or device-namespace shape, or an unreadable ancestor directory). If the directory is inside the worktree ${TOOL_RESULT_BASH_WORKTREE_CWD_UNRESOLVABLE_SPELLING_VAR_0}, re-run the command from its direct symlink-free path.
