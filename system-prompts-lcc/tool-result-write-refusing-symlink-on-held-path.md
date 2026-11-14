<!--
name: 'Tool Result: Write refused, symlink on path'
description: >-
  Error telling Claude a write was refused because a symbolic link is on the
  path, nothing was written, and to check where the path leads before retrying
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_WRITE_REFUSING_SYMLINK_ON_HELD_PATH_VAR_0
-->
Refusing to write ${TOOL_RESULT_WRITE_REFUSING_SYMLINK_ON_HELD_PATH_VAR_0}: a symbolic link is on its path (the file itself, or a directory replaced during the write). Nothing was written there; check where the path leads now and retry.
