<!--
name: 'Slash Command: /ide — no CLI launcher, open manually'
description: >-
  Tells the model the IDE could not be launched programmatically and gives the
  path the user must open by hand, so it stops trying to automate the step.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_0
  - SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_1
  - SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_2
  - SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_3
-->
Please open the ${SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_0?"worktree":"project"} manually in ${SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_1.bold(SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_2.name)}: ${SLASH_COMMAND_IDE_OPEN_MANUALLY_VAR_3}
