<!--
name: 'Tool Result: Bash working directory could not be verified'
description: >-
  Refuses a command when the working directory can no longer be confirmed as the
  permission-checked directory.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_BASH_CWD_UNVERIFIED_BEFORE_SPAWN_VAR_0
-->
Could not confirm that working directory "${TOOL_RESULT_BASH_CWD_UNVERIFIED_BEFORE_SPAWN_VAR_0}" is the directory that this command was permission-checked in (it was deleted, moved, replaced by a link or made unreadable since, it could not be examined, or another command of the same call changed directory), so the command was not run. Re-issue the command to have it checked afresh.
