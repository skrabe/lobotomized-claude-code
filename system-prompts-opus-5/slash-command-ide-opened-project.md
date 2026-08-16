<!--
name: 'Slash Command: /ide — project or worktree opened'
description: >-
  Tells the model the directory was successfully opened in the named editor, and
  whether it was the worktree or the project.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_0
  - SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_1
  - SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_2
-->
Opened ${SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_0?"worktree":"project"} in ${SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_1.bold(SLASH_COMMAND_IDE_OPENED_PROJECT_VAR_2.name)}
