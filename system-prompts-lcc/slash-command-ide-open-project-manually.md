<!--
name: /ide open project manually
description: >-
  Told the model when no IDE launcher is available, asking the user to open the
  project in the IDE themselves.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_0
  - SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_1
  - SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_2
  - SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_3
-->
Open the ${SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_0?"worktree":"project"} in ${SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_1.bold(SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_2.name)} yourself: ${SLASH_COMMAND_IDE_OPEN_PROJECT_MANUALLY_VAR_3}
