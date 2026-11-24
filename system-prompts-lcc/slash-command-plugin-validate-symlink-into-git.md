<!--
name: 'Plugin validate: link into .git'
description: Validation error for a file linking into the repository's .git folder.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_2
  - SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_3
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_0.relative(SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_1,SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_2)} links into the repository's .git folder (${SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_INTO_GIT_VAR_3}). An install doesn't copy what it points at, because those files can change without a new commit. Replace the link with a real file.
