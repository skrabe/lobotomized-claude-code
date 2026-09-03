<!--
name: 'Plugin validate: component directory symlink warning tail'
description: >-
  Tail of the warning saying component directories are not followed through
  symlinks and must be validated at their real path.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_DIR_SYMLINK_WARNING_TAIL_VAR_0
-->
directories are read without following symlinks. A session loading this ${SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_DIR_SYMLINK_WARNING_TAIL_VAR_0==="plugin"?"plugin":"project"} does follow it, so validate the real directory separately.
