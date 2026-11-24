<!--
name: 'Plugin install: copy source inside .git refused'
description: >-
  Error thrown when a plugin copy source lies inside the repository's .git
  folder.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_COPY_SOURCE_IN_GIT_FOLDER_VAR_0
-->
Refusing to copy ${SLASH_COMMAND_PLUGIN_INSTALL_COPY_SOURCE_IN_GIT_FOLDER_VAR_0}: it is inside the repository's .git folder, whose files are not in any commit. The marketplace's author must point this entry at a folder outside .git.
