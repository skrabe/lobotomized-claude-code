<!--
name: 'Tool Result: Write refused, directory replaced by symlink'
description: >-
  Error telling Claude a write was refused because a directory on the path was
  replaced by a symbolic link during the write, nothing was written, and to
  check the path before retrying
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_WRITE_REFUSING_DIRECTORY_REPLACED_BY_SYMLINK_VAR_0
-->
Refusing to write ${TOOL_RESULT_WRITE_REFUSING_DIRECTORY_REPLACED_BY_SYMLINK_VAR_0}: a directory on its path was replaced by a symbolic link during the write. Nothing was written there; check where the path leads now and retry.
