<!--
name: 'Plugin validate: local source inside .git'
description: >-
  Validation error for a marketplace entry whose local source is inside the .git
  folder.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_LOCAL_SOURCE_INSIDE_GIT_VAR_0
-->
Local source "${SLASH_COMMAND_PLUGIN_VALIDATE_LOCAL_SOURCE_INSIDE_GIT_VAR_0}" is inside the repository's .git folder, whose files are not in any commit. Copying it fails, and a commit-pinned marketplace won't load it. Point the entry at a folder outside .git.
