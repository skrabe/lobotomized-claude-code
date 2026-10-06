<!--
name: 'Tool result: write refused, parent directory is a symlink'
description: >-
  Error returned when a file write is refused because the target's parent
  directory is a symlink (checked with O_NOFOLLOW).
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_REFUSING_SYMLINKED_PARENT_DIRECTORY_VAR_0
  - TOOL_RESULT_WRITE_REFUSING_SYMLINKED_PARENT_DIRECTORY_VAR_1
-->
Refusing to write into symlinked directory: ${TOOL_RESULT_WRITE_REFUSING_SYMLINKED_PARENT_DIRECTORY_VAR_0(TOOL_RESULT_WRITE_REFUSING_SYMLINKED_PARENT_DIRECTORY_VAR_1)}
