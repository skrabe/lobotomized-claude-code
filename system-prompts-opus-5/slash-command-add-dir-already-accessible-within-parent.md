<!--
name: 'Slash Command: /add-dir — already covered by an existing working directory'
description: >-
  Tells the model the path is already reachable because an ancestor is a working
  directory, naming that ancestor so it knows the effective access boundary.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_0
  - SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_1
  - SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_2
  - SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_3
-->
${SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_0} is already accessible within ${SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_1} ${SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_2.bold(SLASH_COMMAND_ADD_DIR_ALREADY_ACCESSIBLE_WITHIN_PARENT_VAR_3.workingDir)}.
