<!--
name: 'Plugin validate: component path not a regular file'
description: >-
  Tail of the warning counting components skipped because the path is not a
  regular file.
ccVersion: 2.1.317
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_NOT_REGULAR_FILE_TAIL_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_NOT_REGULAR_FILE_TAIL_VAR_1
-->
regular file (a symlink, a FIFO, a directory). ${SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_NOT_REGULAR_FILE_TAIL_VAR_0==="plugin"?"A FIFO or a directory is never read. ":""}${SLASH_COMMAND_PLUGIN_VALIDATE_COMPONENT_NOT_REGULAR_FILE_TAIL_VAR_1}
