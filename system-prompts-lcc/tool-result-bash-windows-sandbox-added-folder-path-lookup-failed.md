<!--
name: 'Tool Result: Bash Windows sandbox added-folder path lookup failed'
description: >-
  Tells the model the command was not run because a file rule path of a folder
  added this session could not be looked up, and to check the folder or restart
  without it
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_WINDOWS_SANDBOX_ADDED_FOLDER_PATH_LOOKUP_FAILED_VAR_0
  - TOOL_RESULT_BASH_WINDOWS_SANDBOX_ADDED_FOLDER_PATH_LOOKUP_FAILED_VAR_1
-->
Claude Code did not run this command: it could not look up a path that a file rule names for a folder added in this session, such as a worktree (${TOOL_RESULT_BASH_WINDOWS_SANDBOX_ADDED_FOLDER_PATH_LOOKUP_FAILED_VAR_0(TOOL_RESULT_BASH_WINDOWS_SANDBOX_ADDED_FOLDER_PATH_LOOKUP_FAILED_VAR_1)}). Sandboxed commands will keep failing this way while that folder stays added: check that you can open it, or restart Claude Code without it.
