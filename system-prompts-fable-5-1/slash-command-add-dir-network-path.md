<!--
name: 'Slash Command: /add-dir — Network Path'
description: >-
  /add-dir local-jsx onDone text when the path is a network share that cannot be
  added as a working directory.
ccVersion: 2.1.257
variables:
  - SLASH_COMMAND_ADD_DIR_NETWORK_PATH_VAR_0
  - SLASH_COMMAND_ADD_DIR_NETWORK_PATH_VAR_1
-->
${SLASH_COMMAND_ADD_DIR_NETWORK_PATH_VAR_0.bold(SLASH_COMMAND_ADD_DIR_NETWORK_PATH_VAR_1.directoryPath)} is a network path, which cannot be added as a working directory. On Windows, map the share to a drive letter and pass it at launch with --add-dir (a drive letter added mid-session does not yet carry remote-read trust).
