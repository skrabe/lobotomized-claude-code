<!--
name: 'Plugin install: git-subdir path inside .git refused'
description: >-
  Error thrown when a git-subdir plugin entry's path points inside the .git
  folder.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBDIR_IN_GIT_FOLDER_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBDIR_IN_GIT_FOLDER_VAR_1
-->
Refusing to install from ${SLASH_COMMAND_PLUGIN_INSTALL_SUBDIR_IN_GIT_FOLDER_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_SUBDIR_IN_GIT_FOLDER_VAR_1,200)}: it is inside the repository's .git folder, whose files are not in any commit. The marketplace's author must set this entry's path to a folder outside .git.
